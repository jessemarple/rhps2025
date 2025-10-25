# Regenerate the PDF with safer spacing and dynamic row heights to avoid overlap.
# Also render all lines in black for clarity.

import csv, io, re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

csv_text = """Created date (UTC),Amount,Card Name,Card Zip,Customer Email,Checkout Line Item Summary
2025-10-23 20:06:18,50.00,Abigail Clough,99163,abigail.clough4@gmail.com,October 24th @ 8PM (2)
2025-10-06 04:10:40,50.00,Alexandra Pawlik,83861,pawlikalexandra35@gmail.com,October 24th @ 8PM (2)
2025-10-16 16:55:31,25.00,Alicia Woodard,99163,arddycuck@gmail.com,October 24th @ 8PM (1)
2025-10-18 21:48:08,50.00,ANDREW R KOLMAN,99021,juliakolman42@gmail.com,October 24th @ 8PM (2)
2025-10-24 06:06:55,25.00,b.m.pjecha2@gmail.com,99163,b.m.pjecha2@gmail.com,October 24th @ 8PM (1)
2025-10-13 23:10:30,75.00,brooke.bonar99@gmail.com,99163,brooke.bonar99@gmail.com,October 24th @ 8PM (3)
2025-10-13 23:13:51,50.00,cameron.coyle39@gmail.com,99163,cameron.coyle39@gmail.com,October 24th @ 8PM (2)
2025-10-23 12:49:43,50.00,CHARLES PAUL,99163,phantom2145@gmail.com,October 24th @ 8PM (2)
2025-10-23 00:42:11,25.00,Chelsea Osbron,99163,chelsea.osbron@gmail.com,October 24th @ 8PM (1)
2025-10-13 23:28:42,25.00,chhloe13@gmail.com,99163,chhloe13@gmail.com,October 24th @ 8PM (1)
2025-10-16 21:05:53,25.00,Cierra Stokes,83843,cdstokes97@gmail.com,October 24th @ 8PM (1)
2025-10-24 03:56:48,50.00,Cinda Swearengin,83843,winifred.rennant@gmail.com,October 24th @ 8PM (2)
2025-10-24 06:10:48,50.00,Corey Sutter,99163,coreysutterwsu@yahoo.com,October 24th @ 8PM (2)
2025-10-24 04:39:44,25.00,Craig Malone,83843,craigmm114@gmail.com,October 24th @ 8PM (1)
2025-10-14 16:14:23,50.00,Cymon David Dillon,99163,cymon.dillon1965@gmail.com,October 24th @ 8PM (2)
2025-10-18 21:00:44,25.00,Daniel Paul Prestin,98023,prestindaniel@gmail.com,October 24th @ 8PM (1)
2025-10-15 02:49:18,50.00,deandeb75@gmail.com,98848,deandeb75@gmail.com,October 24th @ 8PM (2)
2025-10-16 01:25:16,75.00,douglas park,99161,dpark@palouse.com,October 24th @ 8PM (3)
2025-10-13 23:57:00,25.00,Elizabeth Groetsema,99163,elizabethgale3@gmail.com,October 24th @ 8PM (1)
2025-10-16 22:55:31,100.00,ellescheiderich@gmail.com,93010,ellescheiderich@gmail.com,October 24th @ 8PM (4)
2025-10-08 20:46:11,125.00,eluckenow@gmail.com,99403,eluckenow@gmail.com,October 24th @ 8PM (5)
2025-10-21 17:56:11,25.00,Emma Andersen,83843,emma_albright@hotmail.com,October 24th @ 8PM (1)
2025-10-18 20:55:44,25.00,ethan.dmayo@outlook.com,98032,ethan.dmayo@outlook.com,October 24th @ 8PM (1)
2025-10-21 18:09:12,50.00,faithyv2005@gmail.com,99901,faithyv2005@gmail.com,October 24th @ 8PM (2)
2025-10-24 03:36:57,25.00,garrett.compton@wsu.edu,19350,garrett.compton@wsu.edu,October 24th @ 8PM (1)
2025-10-17 19:51:13,50.00,Grace A Benjamin,83843,grace.a.benjamin@gmail.com,October 24th @ 8PM (2)
2025-10-21 17:45:32,75.00,henry.olsen@wsu.edu,99163,henry.olsen@wsu.edu,October 24th @ 8PM (3)
2025-10-20 01:40:08,50.00,Jack Mayer,83832,jackm8yer@gmail.com,October 24th @ 8PM (2)
2025-09-24 01:31:31,25.00,Jerry L Schutz,83843,siriusidaho@gmail.com,October 24th @ 8PM (1)
2025-10-21 16:04:10,50.00,jlsugai@msn.com,83642,jlsugai@msn.com,October 24th @ 8PM (2)
2025-10-21 04:05:11,50.00,jnbowman1994@gmail.com,83843,jnbowman1994@gmail.com,October 24th @ 8PM (2)
2025-10-19 19:38:14,50.00,jtesnohlidek@gmail.com,83705,jtesnohlidek@gmail.com,October 24th @ 8PM (2)
2025-10-16 23:03:22,25.00,Julie Leavitt,83843,julienleavitt@gmail.com,October 24th @ 8PM (1)
2025-10-22 23:18:53,25.00,Kade Terry,83607,terrya7650@gmail.com,October 24th @ 8PM (1)
2025-10-19 23:39:46,50.00,Kaitlynn Anderson,83843,kma5594@yahoo.com,October 24th @ 8PM (2)
2025-10-22 20:44:36,175.00,Kandice Kambitsch,99164,kandi@wsu.edu,October 24th @ 8PM (7)
2025-10-16 16:54:45,50.00,kari_nelson16@hotmail.com,99163,kari_nelson16@hotmail.com,October 24th @ 8PM (2)
2025-10-22 03:53:07,125.00,kariannthekid@gmail.com,83843,kariannthekid@gmail.com,October 24th @ 8PM (5)
2025-10-16 23:08:25,25.00,Katelyn Hutchinson,83843,katelyn.hutchinson@icloud.com,October 24th @ 8PM (1)
2025-10-16 16:50:06,50.00,Katherine Forsythe,99163,katiemaureen91@hotmail.com,October 24th @ 8PM (2)
2025-10-24 07:37:57,50.00,Kelly Steele,99163,kellysebold@gmail.com,October 24th @ 8PM (2)
2025-10-18 21:03:42,25.00,Kennedy J Parker,98373,cj.parker2626@gmail.com,October 24th @ 8PM (1)
2025-10-21 15:06:15,50.00,Laura Girardeau,83843,beautyofnature.lg@gmail.com,October 24th @ 8PM (2)
2025-10-21 16:18:05,50.00,Lisa Jones,83843,neonroxy@hotmail.com,October 24th @ 8PM (2)
2025-10-20 19:46:00,50.00,mcharboneau12@gmail.com,98087,mcharboneau12@gmail.com,October 24th @ 8PM (2)
2025-10-23 05:26:40,50.00,Miriam Moore,83714,miriammoore7654@gmail.com,October 24th @ 8PM (2)
2025-10-17 19:47:41,50.00,Natalie Warr,83703,natwarr22@gmail.com,October 24th @ 8PM (2)
2025-10-16 16:54:41,25.00,Nitivia Jones,99163,nitiviajunk@gmail.com,October 24th @ 8PM (1)
2025-10-16 22:11:59,50.00,Noah L Aigner,99163,noah.aigner@outlook.com,October 24th @ 8PM (2)
2025-10-17 01:01:42,25.00,Rachel A Horowitz,99163,rachel_a_horowitz@hotmail.com,October 24th @ 8PM (1)
2025-10-15 20:31:22,50.00,Rebecca Liao-Cance,99163,kaitliao@gmail.com,October 24th @ 8PM (2)
2025-10-23 22:17:42,25.00,rose.ruth.thompson@gmail.com,83716,rose.ruth.thompson@gmail.com,October 24th @ 8PM (1)
2025-10-21 01:15:39,50.00,Ryan S Armstrong,83843,nlarmstrong11@gmail.com,October 24th @ 8PM (2)
2025-10-16 01:02:37,50.00,skbruns21@gmail.com,99111,skbruns21@gmail.com,October 24th @ 8PM (2)
2025-10-23 00:49:13,25.00,stacymondy@gmail.com,83843,stacymondy@gmail.com,October 24th @ 8PM (1)
2025-10-19 02:35:54,25.00,Summer Overberg,99403,summer.overberg@gmail.com,October 24th @ 8PM (1)
2025-10-23 21:34:54,75.00,Sydney H Davies,99163,shdavies98@gmail.com,October 24th @ 8PM (3)
2025-10-21 16:31:14,50.00,talithajanette@gmail.com,99179,talithajanette@gmail.com,October 24th @ 8PM (2)
2025-10-23 04:08:54,50.00,Trenton Bann,99403,trentonbann@gmail.com,October 24th @ 8PM (2)
2025-10-17 17:22:06,50.00,yellentine@gmail.com,99111,yellentine@gmail.com,October 24th @ 8PM (2)
"""

# Parse
reader = csv.DictReader(io.StringIO(csv_text))
rows = list(reader)

def extract_tickets(summary: str) -> int:
    m = re.search(r"\((\d+)\)", summary)
    return int(m.group(1)) if m else 1

def is_email(s: str) -> bool:
    return "@" in s and "." in s

entries = []
for r in rows:
    name = r["Card Name"].strip()
    email = r["Customer Email"].strip()
    tickets = extract_tickets(r["Checkout Line Item Summary"])
    entries.append({
        "sort_key": name.lower(),
        "name": name,
        "email": email,
        "tickets": tickets,
        "email_as_name": is_email(name),
    })

entries.sort(key=lambda x: x["sort_key"])

# Layout
W, H = 8.5, 11.0
left, right, top, bottom = 0.7, 0.7, 1.0, 1.0
y_start = H - top

pdf_path = "/mnt/data/WillCall_PreSales_Fri_8PM_v2.pdf"
pp = PdfPages(pdf_path)

def new_page():
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis('off')
    title = "Will-Call Pre-Sales — Friday 8:00 PM — Signature List"
    ax.text(W/2, H - top/2, title, ha="center", va="center", fontsize=16)
    return fig, ax

fig, ax = new_page()
y = y_start - 0.25

for i, e in enumerate(entries):
    # Determine block height
    block_h = 1.4 if e["email_as_name"] else 1.1  # inches
    
    # If not enough space, start a new page
    if y - block_h < bottom:
        pp.savefig(fig)
        plt.close(fig)
        fig, ax = new_page()
        y = y_start - 0.25
    
    # Draw row content
    display = f"{e['name']} ({e['tickets']})"
    ax.text(left, y, display, ha="left", va="top", fontsize=13)
    
    # Small right-justified email for reference
    ax.text(W - right, y, e["email"], ha="right", va="top", fontsize=8)
    
    if e["email_as_name"]:
        ax.text(left, y - 0.25, "(no name given — write legibly)", ha="left", va="top", fontsize=8)
        # Printed name line
        ax.text(left, y - 0.55, "Printed Name:", ha="left", va="top", fontsize=11)
        ax.plot([left + 1.4, W - right], [y - 0.58, y - 0.58], linewidth=0.8, color="black")
        # Signature line
        ax.text(left, y - 0.90, "Signature:", ha="left", va="top", fontsize=11)
        ax.plot([left + 1.05, W - right], [y - 0.93, y - 0.93], linewidth=0.8, color="black")
    else:
        # Signature line only
        ax.text(left, y - 0.55, "Signature:", ha="left", va="top", fontsize=11)
        ax.plot([left + 1.05, W - right], [y - 0.58, y - 0.58], linewidth=0.8, color="black")
    
    # Divider line
    ax.plot([left, W - right], [y - block_h, y - block_h], linewidth=0.5, color="black")
    
    y -= block_h + 0.05  # small extra padding between blocks

# Save last page
pp.savefig(fig)
plt.close(fig)
pp.close()

pdf_path
