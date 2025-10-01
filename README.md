# Simple-Hash-Cracker
A lightweight, educational mini hash cracking tool written in Python.  For ethical use only!! — never use on systems you don't own or have explicit permission to test. — 

## Features
- Automatic hash type detection (MD5, SHA1, SHA256)
- Basic rule-based attack (`password` → `password123`, `password!`, etc.)
- CLI with user-friendly output
- Built-in benchmarking (shows execution time) 
- No external dependencies (uses only Python standard library)

## Usage

### Basic (auto-detect hash type) -- python crack.py <hash> <wordlist>
or you can use '--type' command, example: 'python crack.py wordlist.txt --type md5'

