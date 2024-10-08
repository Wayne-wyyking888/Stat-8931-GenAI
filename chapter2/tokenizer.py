# Source Acknowledgment
# This material includes code modified from Andrej Karpathy's repository available at https://github.com/karpathy/llama2.c.
# The code is used under the Llama 2 Community License Agreement, available at https://ai.meta.com/llama/license/.

import os
import struct
import argparse
from typing import List

from sentencepiece import SentencePieceProcessor

class Tokenizer:
    def __init__(self, tokenizer_model):
        assert os.path.isfile(tokenizer_model), tokenizer_model
        self.sp_model = SentencePieceProcessor(model_file=tokenizer_model)
        self.model_path = tokenizer_model

        # BOS / EOS token IDs
        self.n_words: int = self.sp_model.vocab_size()
        self.bos_id: int = self.sp_model.bos_id()
        self.eos_id: int = self.sp_model.eos_id()
        self.pad_id: int = self.sp_model.pad_id()
        print(f"#words: {self.n_words} - BOS ID: {self.bos_id} - EOS ID: {self.eos_id}")
        assert self.sp_model.vocab_size() == self.sp_model.get_piece_size()

    def encode(self, s: str, bos: bool, eos: bool) -> List[int]:
        assert type(s) is str
        t = self.sp_model.encode(s)
        if bos:
            t = [self.bos_id] + t
        if eos:
            t = t + [self.eos_id]
        return t

    def decode(self, t: List[int]) -> str:
        return self.sp_model.decode(t)
