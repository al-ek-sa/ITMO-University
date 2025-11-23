# Author = Lishik Aleksandra Yuryevna
# Group = P3106
# Date = 07.11.2025
# Option 503302%132=118
# Task 1.3

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
        while self.symbol and self.symbol in ' \t\n':
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
            if self.symbol in ' \t\n':
                self.cancellation()
                continue
            
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
            block = self.token_future.value
            self.next_token()
            id = ""
            if self.token_future.type == TokenType.String:
                id = self.token_future.value
                self.next_token()
            self.next_token()
            content = self.list()
            self.next_token()
            key = f"{block} {id}".strip()
            result[key] = content
        return result

    def list(self):
        content = {}
        while self.token_future.type not in [TokenType.Rbrace, TokenType.EOF]:
            key = self.token_future.value
            self.next_token()
            if self.token_future.type == TokenType.Equals:
                self.next_token()
                value = self.parse_values()
                content[key] = value
            else:
                id = ""
                if self.token_future.type == TokenType.String:
                    id = self.token_future.value
                    self.next_token()
                self.next_token()  
                nested_content = self.list()
                self.next_token()  
                nested_key = f"{key} {id}".strip()
                content[nested_key] = nested_content
        return content

    def parse_values(self):
        token = self.token_future
        if token.type == TokenType.String:
            self.next_token()
            return token.value
        elif token.type == TokenType.Number:
            self.next_token()
            return float(token.value) if '.' in token.value else int(token.value)
        elif token.type == TokenType.Boolean:
            self.next_token()
            return token.value == 'true'
        elif token.type == TokenType.Lbrace:
            self.next_token()
            obj_content = self.list()
            self.next_token()  
            return obj_content
        else:
            self.next_token()
            return token.value

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


class XML:
    @staticmethod
    def serialize(data, nameroot="root"):
        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        XML._xml(data, nameroot, xml, 0)
        return '\n'.join(xml)
    @staticmethod
    def _xml(data, replacing, xml, level):
        retreat = '  ' * level
        replacing_spaces = replacing.replace(' ', '_')
        if isinstance(data, dict):
            xml.append(f'{retreat}<{replacing_spaces}>')
            for key, value in data.items():
                XML._xml(value, str(key), xml, level + 1)
            xml.append(f'{retreat}</{replacing_spaces}>')
        elif isinstance(data, list):
            xml.append(f'{retreat}<{replacing_spaces}>')
            for i, item in enumerate(data):
                XML._xml(item, f"item_{i}", xml, level + 1)
        else:
            value = str(data)
            value = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            xml.append(f'{retreat}<{replacing_spaces}>{value}</{replacing_spaces}>')
    @staticmethod
    def save_to_file(data, filename, nameroot ="root"):
        xml = XML.serialize(data, nameroot)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml)

class FileReader:
    @staticmethod
    def read_file(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()

def main():
    try:
        hcl_content = FileReader.read_file("doc.hcl")
        parser = Parser(hcl_content)
        parsed = parser.parse()
        print(parsed)
        binary_data = Binary.serialize(parsed)
        print(binary_data)
        deserializer = Deserialize(binary_data)
        data = deserializer.deserialize()
        xml_content = XML.serialize(data, "configuration")
        print(xml_content)
        XML.save_to_file(data, "doc.xml")
    except Exception as e:
        print(f"Error: {e}")
        return
if __name__ == "__main__":
    main()