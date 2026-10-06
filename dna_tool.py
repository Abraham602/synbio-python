def gc_content(seq):
    """返回 GC 含量（0 到 1 之间的小数）"""
    g = seq.count("G")
    c = seq.count("C")
    return (g + c) / len(seq)
    pass

def reverse_complement(seq):
    """返回反向互补序列"""
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    newseq = ""
    for ch in seq[::-1]:
        newseq += comp[ch]
    return newseq
    pass

def transcribe(seq):
    """DNA → RNA（T 换成 U）"""
    return seq.replace("T","U")
    pass

def translate(seq):
    """DNA → 蛋白质（每3个碱基翻译成1个氨基酸，遇终止密码子停）"""
    # 用字典存密码子表
    codon_table = {
        "ATG": "M", "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L",
    # ... 至少补全常见氨基酸
        "TAA": "Stop", "TAG": "Stop", "TGA": "Stop",
    }

    # 每次取 3 个字符，查表
    protein = ""
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        aa = codon_table.get(codon, "?")
        if aa == "Stop":
            break
        protein += aa
    return protein
    pass





if __name__ == "__main__":
    seq = "ATGGCTTAAGCT"
    print("原始序列:", seq)
    print("GC含量:", gc_content(seq))            # 期望约 0.4167
    print("反向互补:", reverse_complement(seq))  # 期望 AGCTTAAGCCAT
    print("转录RNA:", transcribe(seq))           # 期望 AUGGCUUAAGCU
    print("翻译蛋白:", translate(seq))           # 期望 MA