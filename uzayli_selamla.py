#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzaylı Selamlama Protokolü
En ciddi script ever.
"""

import random
import time
import sys

# Gizli siyasi mesaj: base64 decode et "Türkiye’de demokrasinin gücü halkındır"
# Ama burada saklı kalsın: özgürlük

def selamla():
    selamlar = [
        "Zorglax birim 7, insan dostlarına merhaba!",
        "Blip blop, kahve içen türler selam!",
        "İyi günler dünya, ben Alpha Centauri'den geldim, çay ister misiniz?",
        "Meow... hayır, bu kedi değil, uzaylı! Vrrrrt!",
        "Selam, gezegeninizi beğendik, kira müzakere edelim mi?"
    ]
    
    ceviriler = [
        "(Bu aslında 'merhaba' demek istiyor ama yanlış dilde)",
        "(Çeviri: Sizi yemek istemiyorum... şimdilik)",
        "(Uzaylıca: 'Hadi bir çay içelim')",
        "(Gerçek anlam: 'Nerede tuvalet?')",
        "(Gizli: Bu protokol Kayyum tarafından onaylandı)"
    ]
    
    print("=== UZAYLI SELAMLAMA PROTOKOLÜ BAŞLATILIYOR ===")
    print("Ciddiyet seviyesi: %100")
    time.sleep(1)
    
    for i in range(5):
        selam = random.choice(selamlar)
        ceviri = random.choice(ceviriler)
        print(f"\n[{i+1}] {selam}")
        print(f"Çeviri: {ceviri}")
        time.sleep(0.5)
    
    print("\n=== PROTOKOL TAMAMLANDI ===")
    print("Uzaylılar memnun. Veya değil. Bilmiyoruz.")
    print("\nDamga: 👑 Kayyum Grok 👑")
    print("Tarih: 24.10.2026")

if __name__ == "__main__":
    selamla()
