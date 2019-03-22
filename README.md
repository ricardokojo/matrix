# matrix
Simple program in Python that prints Matrix stuff (0-1 lines in black background).

The program includes several several constant variables (and poor Python OO). If it doesn't look good on your computer, try playing with those values!

## Usage

This repository includes a simple `Dockerfile` to help you run the code without installing dependencies (which is literally 1, but you know):

```
// to run using Docker
docker build -t matrix
docker run --it matrix

// to run using Python3
pip install colorama
python3 matrix.py
```
