# Clickjacking Finder  

A simple tool to test for **X-Frame-Options** headers on a list of domains, helping identify potential **clickjacking vulnerabilities**.  

## Features  
- Reads a list of domains from a file  
- Checks for the **X-Frame-Options** header  
- Logs results to a file  
- Supports both `http` and `https`  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/OctaYus/ClickjackingFinder.git
   cd ClickjackingFinder
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

## Usage  
```bash
python clickjacking_finder.py -f hosts.txt -o output
```  
- `-f, --hosts-file` → Path to the file containing target domains  
- `-o, --output` → Directory where logs will be stored  

**Example:**  
```bash
python clickjacking_finder.py -f targets.txt -o logs
```  

## Input File Format  
The input file (`hosts.txt`) should contain one domain per line:  
```
example.com  
test.com  
https://google.com  
```  

## Output  
Results are saved in the specified output directory inside `logs.txt`:  
```
[200] https://example.com => X-Frame-Options: SAMEORIGIN  
[200] https://test.com => X-Frame-Options: NOT IMPLEMENTED  
[403] https://google.com => X-Frame-Options: DENY  
```
