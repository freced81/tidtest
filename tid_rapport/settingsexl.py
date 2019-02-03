# WIDTH IN mm
colum_width_settings = {
    "A": 13,
    "B": 13,
    "C": 56,
    "D": 10,
    "E": 10,
    "F": 10,
    "G": 10,
    "H": 10,
    "I": 10,
    "J": 10,
    "K": 16,
    "L": 16,
    "M": 16,
    "N": 10,
    "O": 10,
    "P": 14,
    "Q": 14,
    "R": 14,
}
# HEIGT IN mm
row_heigt_settings = {
    "1": 6,
    "2": 6.5,
    "3": 4,
    "4": 6.5,
    "5": 4,
    "6": 6.5,
    "7": 6.5,
    "8": 6.5,
    "9": 6.5,
    "10": 6.5,
    "11": 6.5,
    "12": 6.5,
    "13": 6.5,
    "14": 6.5,
    "15": 6.5,
    "16": 6.5,
    "17": 6.5,
    "18": 6.5,
    "19": 6.5,
    "20": 6.5,
    "21": 6,
}
merge_cells_settings = [
    "A1:D1",  # LOGGA
    "A2:D2",  # LOGGA
    "E1:J2",  # TIDUPGIFT
    "K1:L1",  # DATUM FRÅN
    "K2:L2",  # DATUM FRÅN
    "M1:N1",  # DATUM TILL
    "M2:N2",  # DATUM TILL
    "O1:R1",  # VECKA NR
    "O2:R2",  # VECKA NR
    "A3:G3",  # MONTÖR NAMN
    "A4:G4",  # MONTÖR NAMN
    "H3:J3",  # ORDERNR
    "H4:J4",  # ORDERNR
    "K3:R3",  # ANLÄGGNING
    "K4:R4",  # ANLÄGGNING
    "A5:G5",  # KUND
    "A6:G6",  # KUND
    "H5:R5",  # ARBETSPLATS
    "H6:R6",  # ARBETSPLATS
    "A21:K21",  # SUMMA
]
font_settings = {
    "A1": "font_logga",
    "A2": "font_logga",
    "E1": "font_tiduppgift",
    "K1": "font_small",
    "K2": "font_normal",
    "M1": "font_small",
    "M2": "font_normal",
    "O1": "font_small",
    "O2": "font_normal",
    "A3": "font_small",
    "A4": "font_normal",
    "H3": "font_small",
    "H4": "font_normal",
    "K3": "font_small",
    "K4": "font_normal",
    "A5": "font_small",
    "A6": "font_normal",
    "H5": "font_small",
    "H6": "font_normal",
    "A7": "font_head",
    "B7": "font_head",
    "C7": "font_head",
    "D7": "font_head",
    "E7": "font_head",
    "F7": "font_head",
    "G7": "font_head",
    "H7": "font_head",
    "I7": "font_head",
    "J7": "font_head",
    "K7": "font_head",
    "L7": "font_head",
    "M7": "font_head",
    "N7": "font_head",
    "O7": "font_head",
    "P7": "font_head",
    "Q7": "font_head",
    "R7": "font_head",
}
font_normal_settings = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
]


set_initial_text = {
    "A1": "Skandinavisk Process",
    "A2": "Automation AB",
    "E1": "TIDUPPGIFT",
    "K1": "Datum fr.o.m",
    "M1": "Datum t.o.m",
    "O1": "Vecka Nr",
    "A3": "Montörens Namn",
    "H3": "Order Nr",
    "K3": "Anläggning",
    "A5": "Kund",
    "H5": "Arbetsplats",
    "A7": "Vecka",
    "B7": "Ordnr",
    "C7": "Beskrivning",
    "D7": "Må",
    "E7": "Ti",
    "F7": "On",
    "G7": "To",
    "H7": "Fr",
    "I7": "Lö",
    "J7": "Sö",
    "K7": "Restid",
    "L7": "Totaltid",
    "M7": "För lön",
    "N7": "Ö1",
    "O7": "Ö2",
    "P7": "Trakt",
    "Q7": "Pmil",
    "R7": "Fmil",
    "A21": "Summa denna vecka ",
}
border_font_normal = [
    "K2",
    "M2",
    "O2",
    "A4",
    "H4",
    "K4",
    "A6",
    "H6",
    "L21",
    "M21",
    "N21",
    "O21",
    "P21",
    "Q21",
    "R21",
]
formula_tot = ["L", "M"]
summa_tot = {
    "L21": "=SUM(L8:L20)",
    "M21": "=SUM(M8:M20)",
    "N21": "=SUM(N8:N20)",
    "O21": "=SUM(O8:O20)",
    "P21": "=SUM(P8:P20)",
    "Q21": "=SUM(Q8:Q20)",
    "R21": "=SUM(R8:R20)",
}
