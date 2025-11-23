# Author = Lishik Aleksandra Yuryevna
# Group = P3106
# Date = 07.11.2025
# Option 503302%132=118
# Task 1 - 1.1

import struct
from enum import Enum


class TokenType(Enum):
    Identifier = "Identifier"
    String = "String"
    Number = "Number"
    Boolean = "Boolean"
    Lbrace = "Lbrace"
    Rbrace = "Rbrace"
    Comma = "Comma"
    Lbracket = "Lbracket"
    Rbracket = "Rbracket"
    Equals = "Equals"
    EOF = "EOF"
    Newline = "Newline"


class Token:
    def __init__(self, type: TokenType, value: str = ""):
        self.type = type
        self.value = value
        
    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}')"
        
        
class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.position = 0
        if text:
            self.symbol = self.text[0]
        else:
            self.symbol = None 
            
    def next(self):
        self.position += 1
        if self.position < len(self.text):
            self.symbol = self.text[self.position]
        else:
            self.symbol = None
                    
    def cancellation(self):
        while self.symbol and self.symbol in ' \t':
            self.next()
            
    def quotation_marks(self):
        self.next()
        result = ""
        while self.symbol and self.symbol != '"':
            result += self.symbol
            self.next()
        if self.symbol == '"':
            self.next()
        return result
        
    def read(self):
        result = ""
        while self.symbol and (self.symbol in '_-".' or self.symbol.isalpha() or self.symbol.isnumeric()):
            result += self.symbol
            self.next()
        return result
    
    def is_number(self, value):
        if not value:
            return False
        if value in ['true', 'false']:
            return False
        if value.count('.') > 1:
            return False
        without_dots = value.replace('.', '')
        if without_dots and without_dots.isdigit():
            return True
        return False
    
    def token_next(self):
        while self.symbol:
            if self.symbol in ' \t':
                self.cancellation()
                continue
            if self.symbol == '\n':
                self.next()
                return Token(TokenType.Newline, '\n')
            if self.symbol == '"':
                return Token(TokenType.String, self.quotation_marks())
            if self.symbol in '_-"' or self.symbol.isalpha() or self.symbol.isnumeric():
                value = self.read()
                if value in ['true', 'false']:
                    return Token(TokenType.Boolean, value)
                elif self.is_number(value):
                    return Token(TokenType.Number, value)
                else:
                    return Token(TokenType.Identifier, value)
            if self.symbol == '{':
                self.next()
                return Token(TokenType.Lbrace, '{')
            if self.symbol == '}':
                self.next()
                return Token(TokenType.Rbrace, '}')
            if self.symbol == '[':
                self.next()
                return Token(TokenType.Lbracket, '[')
            if self.symbol == ']':
                self.next()
                return Token(TokenType.Rbracket, ']')
            if self.symbol == '=':
                self.next()
                return Token(TokenType.Equals, '=')
            if self.symbol == ',':
                self.next()
                return Token(TokenType.Comma, ',')
            self.next()
        return Token(TokenType.EOF)
    
class Parser:
    def __init__(self, text: str):
        self.lexer = Lexer(text)
        self.token_future = self.lexer.token_next()
        
    def next_token(self):
        self.token_future = self.lexer.token_next()
        
    def parse(self):
        result = {}
        while self.token_future.type != TokenType.EOF:
            if self.token_future.type == TokenType.Identifier:
                block_name = self.token_future.value
                self.next_token()
                block_id = ""
                if self.token_future.type == TokenType.String:
                    block_id = self.token_future.value
                    self.next_token()
                if self.token_future.type == TokenType.Lbrace:
                    self.next_token()
                    block_content = self.parse_block()
                    if self.token_future.type == TokenType.Rbrace:
                        self.next_token()
                    
                    key = f"{block_name} {block_id}".strip()
                    result[key] = block_content
                else:
                    raise SyntaxError(f"Expected '{{' after {block_name} {block_id}")
            else:
                self.next_token()
        return result
    
    def parse_block(self):
        content = {}
        while self.token_future.type not in [TokenType.Rbrace, TokenType.EOF]:
            if self.token_future.type == TokenType.Identifier:
                key = self.token_future.value
                self.next_token()
                if self.token_future.type == TokenType.Equals:
                    self.next_token()
                    value = self.parse_value()
                    content[key] = value
                elif self.token_future.type == TokenType.Lbrace:
                    self.next_token()
                    nested_content = self.parse_block()
                    if self.token_future.type == TokenType.Rbrace:
                        self.next_token()
                    content[key] = nested_content
                elif self.token_future.type == TokenType.String:
                    nested_id = self.token_future.value
                    self.next_token()
                    
                    if self.token_future.type == TokenType.Lbrace:
                        self.next_token()
                        nested_content = self.parse_block()
                        if self.token_future.type == TokenType.Rbrace:
                            self.next_token()
                        nested_key = f"{key} {nested_id}".strip()
                        content[nested_key] = nested_content
                    else:
                        raise SyntaxError(f"Expected '{{' after {key} {nested_id}")
                else:
                    continue
            else:
                self.next_token()
        return content 
    
    def parse_value(self):
        if self.token_future.type == TokenType.String:
            value = self.token_future.value
            self.next_token()
            return value
            
        elif self.token_future.type == TokenType.Number:
            value = float(self.token_future.value) if '.' in self.token_future.value else int(self.token_future.value)
            self.next_token()
            return value
            
        elif self.token_future.type == TokenType.Boolean:
            value = self.token_future.value == 'true'
            self.next_token()
            return value
            
        elif self.token_future.type == TokenType.Lbrace:
            self.next_token()
            obj_content = self.parse_block()
            if self.token_future.type == TokenType.Rbrace:
                self.next_token()
            return obj_content
            
        elif self.token_future.type == TokenType.Newline:
            self.next_token()
            return ""
            
        else:
            value = self.token_future.value if hasattr(self.token_future, 'value') else ""
            self.next_token()
            return value
        
class Binary:
    @staticmethod
    def serialize(data):
        if isinstance(data, str):
            encoded = data.encode('utf-8')
            return b's' + struct.pack('I', len(encoded)) + encoded
        elif isinstance(data, bool):
            return b'b' + (b'\x01' if data else b'\x00')
        elif isinstance(data, (int, float)):
            if isinstance(data, int):
                return b'i' + struct.pack('q', data)
            else:
                return b'f' + struct.pack('d', data)
        elif isinstance(data, dict):
            result = b'd' + struct.pack('I', len(data))
            for key, value in data.items():
                result += Binary.serialize(key)
                result += Binary.serialize(value)
            return result
        elif isinstance(data, list):
            result = b'l' + struct.pack('I', len(data))
            for item in data:
                result += Binary.serialize(item)
            return result
        elif data is None:
            return b'n'
        else:
            raise ValueError(f"Unsupported type: {type(data)}")
        
        
class Deserialize:
    def __init__(self, data):
        self.data = data
        self.position = 0
        
    def read(self, x):
        result = self.data[self.position:self.position + x]
        self.position += x
        return result
    
    def deserialize(self):
        byte = self.read(1)
        
        if byte == b's':  
            length = struct.unpack('I', self.read(4))[0]
            return self.read(length).decode('utf-8')
        elif byte == b'b':  
            return self.read(1) == b'\x01'
        elif byte == b'i':  
            return struct.unpack('q', self.read(8))[0]
        elif byte == b'f':  
            return struct.unpack('d', self.read(8))[0]
        elif byte == b'd':  
            length = struct.unpack('I', self.read(4))[0]
            return {self.deserialize(): self.deserialize() for _ in range(length)}
        elif byte == b'l': 
            length = struct.unpack('I', self.read(4))[0]
            return [self.deserialize() for _ in range(length)]
        elif byte == b'n':
            return None


class INI:
    @staticmethod
    def serialize(data):
        result = []
        for main_key, main_value in data.items():
            if " " in main_key:
                parts = main_key.split(" ", 1)
                section_type = parts[0]
                name = parts[1]
                result.append(f"[{section_type}]")
                result.append(f"name = {name}")
                result.append("")
            INI._process_dict(main_value, result, [])
        return "\n".join(result)
    @staticmethod
    def _process_dict(data, result, path):
        if not isinstance(data, dict):
            return
        simple_pairs = {}
        nested_blocks = {}
        for key, value in data.items():
            if isinstance(value, dict):
                nested_blocks[key] = value
            else:
                simple_pairs[key] = value
        if simple_pairs and path:
            section_name = ".".join(path)
            result.append(f"[{section_name}]")
            for key, value in simple_pairs.items():
                result.append(f"{key} = {value}")
            result.append("")
        for key, value in nested_blocks.items():
            INI._process_dict(value, result, path + [key])


class FileReader:
    @staticmethod
    def read_file(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
def main():
    try:
        hcl_content = FileReader.read_file("doc.hcl")
        parser = Parser(hcl_content)
        parsed_data = parser.parse()
        print(parsed_data)
        binary_data = Binary.serialize(parsed_data)
        print(f"{binary_data}")
    except Exception as e:
        print(f"{e}")
        return
    deserializer = Deserialize(binary_data)
    data = deserializer.deserialize()
    ini_content = INI.serialize(data)
    with open("doc.ini", "w", encoding="utf-8") as f:
        f.write(ini_content)
    print(ini_content)
if __name__ == "__main__":
    main()