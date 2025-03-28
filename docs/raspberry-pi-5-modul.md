---
title: Raspberry Pi 5 modul
layout: default
nav_order: 3
---

# Modul pro Raspberry Pi 5

---

## **Příprava**

- Budete potřebovat modely:
    - *module_raspberry-pi-5_front*
    - *module_raspberry-pi-5_base*
    - 2x *assets_module_mount*
{: .step}

- Dále budete potřebovat materiály:
    - lepidlo
    - 8x závitové vložky M3x3
    - 4x závitové vložky M2,5x4
    - 6x šrouby M2,5x7
    - 2x matice M2,5
    - 8x šrouby M3x8 se zkosenou hlavou
    - 80g filamentu
{: .step}

- Použitá elektronika:
    - Raspberry Pi 5
    - [I2C 0,96" OLED displej](https://www.amazon.co.uk/dp/B06XRBTBTB)
    - [Tlakový spínač bez aretace 12mm](https://www.amazon.co.uk/Black-Momentary-Square-Button-Switch/dp/B07CZL13JZ) s připájenými propojovacími kabely (20 cm)
    - [Rotační enkodér s tlačítkem](https://www.amazon.co.uk/Youmile-Encoder-Encoding-Potentiometer-Rotating/dp/B0BN5M3P4P)
    - Propojovací kabely 15-20cm samec-samice

- Použité nástroje:
    - pájecí stanice
    - šroubovák
{: .step}

---

## **Krok 1:** Tisk
![alt](/images/rpi5_print1.png){: .col}
- Položte modely na tiskovou podložku tak, jak je ukázané na obrázku.
- U modelu *module_raspberry-pi-5_front* přidejte podpěry pod držák na displej, v PrusaSliceru stačí, když je automaticky vygenerujete přes nástroj kreslení podpěr
{: .col}
<br style="clear: left;" />

---

## **Krok 2:** Závitové vložky
![alt](/images/P1470422.JPG){: .col}
- Zaveďte do stran modelu *module_raspberry-pi-5_front* závitové vložky M3x3
{: .col}
<br style="clear: left;" />

![alt](/images/P1470425.JPG){: .col}
- Do modelu *module_raspberry-pi-5_base* přidejte závitové vložky M2,5x4 podle obrázku
{: .col}
<br style="clear: left;" />

---

## **Krok 3:** Lepení
![alt](/images/P1470427.JPG){: .col}
- Slepte modely *module_raspberry-pi-5_front* a *module_raspberry-pi-5_base* podle obrázku
{: .col}
<br style="clear: left;" />

---

## **Krok 4:** Instalace elektroniky
![alt](/images/P1470434.JPG){: .col}
- Pomocí šroubů M2,5x7 přidělejte Raspberry Pi 5
- Vsuňte displej podle obrázku a pomocí šroubů M2,5x7 a matic M2,5 ho mírně přidělejte
{: .col}
<br style="clear: left;" />

![alt](/images/P1470438.JPG){: .col}
- Nainstalujte tlakový spínač a rotační enkodér
{: .col}
<br style="clear: left;" />

---

## **Krok 5:** Zapojení
![alt](/images/P1470440.JPG){: .col}
- Zapojení displeje:
    - GND -> Pin 9
    - VCC -> Pin 1
    - SLC -> Pin 5
    - SDA -> Pin 3
- Zapojení rotačního ekodéru:
    - GND -> Pin 6
    - S1 -> Pin 11
    - S2 -> Pin 12
    - Key -> Pin 13
    - 5V -> Pin 2
- Kabely tlačítka připojte na piny napájecího tlačítka Raspberry Pi 5
{: .col}
<br style="clear: left;" />

---

## **Krok 6:** Připevnění 
![alt](/images/P1470442.JPG){: .col}
- Připevněte model *assets_module_mount* pomocí čtyř M3x8 šroubů se zkosenou hlavou
- Stejně to zopakujte na druhé straně
{: .col}
<br style="clear: left;" />

---

[Další](../network-modul)