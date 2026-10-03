import sys
def print_duplicate_characters():
    s=sys.stdin.read().strip()
    if not s:
        print("No duplicates")
        return
    seen_mask=0
    duplicate_mask=0
    for char in s:
        bit=ord(char)-ord('a')
        if (seen_mask &(1<<bit))!=0:
            duplicate_mask |=(1<<bit)  
        else:
            seen_mask |=(1<<bit)   
    printed_mask=0
    result=[]
    for char in s:
        bit=ord(char)-ord('a')
        if (duplicate_mask & (1 << bit)) != 0 and (printed_mask & (1 << bit)) == 0:
            result.append(char)
            printed_mask |= (1 << bit) 
    if result:
        print(" ".join(result))
    else:
        print("No duplicates")

if __name__ == '__main__':
    print_duplicate_characters()
