"""
Module for generating Question-Answer pairs using Groq API
"""
import os
from typing import List, Dict, Optional
from groq import Groq


class QnAGenerator:
    """Generate QnA pairs using Groq API (Free tier: 10,000 requests/day!)"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize QnA Generator with Groq
        
        Args:
            api_key: Groq API key (if None, uses GROQ_API_KEY env variable)
        """
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        
        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"  # Updated - mixtral was decommissioned
        print(f"✅ Groq API initialized with model: {self.model}")
        print(f"✅ Free tier quota: 10,000 requests/day!")
    
    def generate_qna_from_text(self, text: str, num_questions: int = 5) -> List[Dict[str, str]]:
        """
        Generate QnA pairs from input text
        
        Args:
            text: Input text to generate QnA from
            num_questions: Number of QnA pairs to generate
            
        Returns:
            List of dictionaries with 'question' and 'answer' keys
        """
        try:
            # Truncate text if too long
            max_chars = 8000
            if len(text) > max_chars:
                text = text[:max_chars]
            
            prompt = f"""Generate exactly {num_questions} Question-Answer pairs from this text. Use this format exactly:

Q1: [Question]
A1: [Answer]
Q2: [Question]
A2: [Answer]

Questions should be clear and answerable from the text. Answers should be concise and derived from the text.

TEXT:
{text}

RESPONSE (use format above):"""
            
            print(f"   Calling Groq API for {num_questions} questions...")
            
            # Call Groq API
            message = self.client.chat.completions.create(
                messages=[
                    {"role": "user", "content": prompt}
                ],
                model=self.model,
                temperature=0.5,  # Lower temp for more consistent format
                max_tokens=2000,
            )
            
            response_text = message.choices[0].message.content
            print(f"   Response received ({len(response_text)} chars)")
            
            qna_pairs = self._parse_qna_response(response_text)
            
            return qna_pairs
        
        except Exception as e:
            print(f"   ❌ Groq API error: {str(e)}")
            raise Exception(f"Error generating QnA with Groq: {str(e)}")
    
    def _parse_qna_response(self, response_text: str) -> List[Dict[str, str]]:
        """
        Parse the LLM response to extract QnA pairs
        Handles multiple format variations
        
        Args:
            response_text: Raw response from LLM
            
        Returns:
            List of parsed QnA dictionaries
        """
        qna_pairs = []
        lines = response_text.strip().split('\n')
        
        current_question = None
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            
            # Skip empty lines
            if not line:
                continue
            
            # Match Q1: Q2: etc or just Q: A:
            if line and (line[0] in ['Q', 'q']) and ':' in line:
                # Extract question (everything after the colon)
                parts = line.split(':', 1)
                if len(parts) > 1:
                    current_question = parts[1].strip()
            
            # Match A1: A2: etc or just A:
            elif line and (line[0] in ['A', 'a']) and ':' in line and current_question:
                # Extract answer
                parts = line.split(':', 1)
                if len(parts) > 1:
                    answer = parts[1].strip()
                    qna_pairs.append({
                        'question': current_question,
                        'answer': answer
                    })
                    current_question = None
        
        # Debug: Print what was parsed
        if qna_pairs:
            print(f"   ✓ Parsed {len(qna_pairs)} QnA pairs from response")
        else:
            print(f"   ⚠️ No QnA pairs parsed. Response preview:")
            print(f"      {response_text[:200]}...")
        
        return qna_pairs
    
    def generate_qna_batch(self, text_chunks: List[str], num_questions_per_chunk: int = 3) -> List[Dict[str, str]]:
        """
        Generate QnA pairs from multiple text chunks
        Divides entire document into 5 evenly-spaced chunks for full coverage
        
        Args:
            text_chunks: List of text chunks
            num_questions_per_chunk: Number of QnA pairs per chunk
            
        Returns:
            Combined list of QnA pairs
        """
        all_qna = []
        
        MAX_CHUNKS = 5
        
        # Divide entire document into 5 chunks evenly spread
        if len(text_chunks) > MAX_CHUNKS:
            # Calculate step size to sample evenly across document
            step = len(text_chunks) // MAX_CHUNKS
            # Get indices: [0, step, 2*step, 3*step, 4*step]
            indices = [i * step for i in range(MAX_CHUNKS)]
            chunks_to_process = [text_chunks[idx] for idx in indices]
            print(f"📝 Dividing {len(text_chunks)} chunks into {MAX_CHUNKS} evenly-spaced samples")
            print(f"   Sampling indices: {indices}")
        else:
            # If document has fewer chunks than 5, process all
            chunks_to_process = text_chunks
            print(f"📝 Processing all {len(text_chunks)} chunks from document")
        
        for i, chunk in enumerate(chunks_to_process, 1):
            if chunk.strip():
                try:
                    print(f"\n   Chunk {i}/{len(chunks_to_process)}:")
                    qna_pairs = self.generate_qna_from_text(chunk, num_questions_per_chunk)
                    all_qna.extend(qna_pairs)
                    print(f"   ✅ Total QnA pairs so far: {len(all_qna)}")
                except Exception as e:
                    print(f"   ❌ Error: {str(e)}")
                    continue
        
        print(f"\n📊 Total QnA pairs generated: {len(all_qna)}")
        return all_qna
