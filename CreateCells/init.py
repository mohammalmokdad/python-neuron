def init(h):
    soma=h.Section(name="soma")
    soma.insert('pas')
    soma.insert("gh")
    soma.insert('na3rp')
    soma.insert('naps')
    soma.insert('kdrRL')
    soma.insert('mAHP')

    dend=h.Section(name="dend")
    dend.connect(soma,0)
    dend.insert('pas')
    dend.insert("gh")
    dend.insert('L_Ca')
    dend.insert('kca2')
    return soma,dend