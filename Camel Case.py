import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    pattern=input_data[-1]
    raw_words=input_data[1:-1]
    words=[]
    for item in raw_words:
        words.extend([w for w in item.split(',') if w])
    matched=[]
    for word in words:
        abbr="".join([c for c in word if c.isupper()])
        if abbr.startswith(pattern):
            matched.append((abbr, word))
    if not matched:
        print("No match found")
        return
    matched.sort(key=lambda x: (x[0], x[1]))
    print(" ".join([word for abbr, word in matched]))
if __name__ == '__main__':
    solve()
