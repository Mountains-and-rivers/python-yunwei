text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
def avg_word_length(alist):
    ns = []
    for i in text:
        chars = 0
        for j in i:

            if not ('a' <= j <= 'z' or 'A' <= j <= 'Z'):
                if chars !=0:
                    ns.append(chars)
                chars = 0
            else:
                chars += 1
    return sum(ns)/len(ns)
print(avg_word_length(text))