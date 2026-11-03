from django.shortcuts import render
from .models import SeatingTable

def detay(request):
    return render(request, 'envite/detay.html')

# Create your views here.

def rejis(request):
    return render(request, 'envite/rejis.html')

def maryaj(request):
    return render(request, 'envite/maryaj.html')

def lakay(request):
    return render(request, 'envite/lakay.html')

def rad(request):
    return render(request, 'envite/rad.html')

def vwayaj(request):
    return render(request, 'envite/vwayaj.html')

def istwanou(request):
    return render(request, 'envite/istwanou.html')

def kesyon(request):
    return render(request, 'envite/kesyon.html')

# Positions were measured directly on floorplan.jpeg (622 x 1240 reference
# pixels) and converted to percentages, so they scale with the image.
IMG_W, IMG_H = 622, 1240
 
# Fallback: marker at the table's label (x, y)
TABLE_LABELS = {
    0: (295, 122), 1: (485, 1062), 2: (95, 1057), 3: (370, 814), 4: (235, 817),
    5: (470, 564), 6: (105, 574), 7: (355, 354), 8: (235, 372),
    9: (485, 172), 10: (105, 152),
}
 
# y of every chair along one side of the table, starting at the end nearest
# the head table. Seats: 1 = inside #1, 2 = outside #1, 3 = inside #2, ...
CHAIR_Y = {
    10: [107, 138, 169, 200, 231],
    9:  [107, 138, 169, 200, 231],
    8:  [268, 295, 321, 348, 382, 409, 436, 463],
    7:  [268, 295, 321, 348, 382, 409, 436, 463],
    6:  [497, 524, 551, 578, 613, 640, 667, 694],
    5:  [497, 524, 551, 578, 613, 640, 667, 694],
    4:  [728, 755, 782, 809, 844, 871, 898, 925],
    3:  [728, 755, 782, 809, 844, 871, 898, 925],
    2:  [959, 986, 1013, 1040, 1074, 1101, 1129, 1156],
    1:  [959, 986, 1013, 1040, 1074, 1101, 1129, 1156],
}
 
LEFT_TABLES = {10, 8, 6, 4, 2}
INSIDE_X = {True: 177.5, False: 402.5}    # left-column tables / right-column tables
OUTSIDE_X = {True: 135.5, False: 444.5}
 
 
def _pct(x, y):
    return (round(x / IMG_W * 100, 1), round(y / IMG_H * 100, 1))
 
 
def seat_spot(table_num, seat):
    """Return (x%, y%) for a table number and seat number, or None."""
    ys = CHAIR_Y.get(table_num)
    if not ys or not seat or not 1 <= seat <= 2 * len(ys):
        return None
    left = table_num in LEFT_TABLES
    inside = seat % 2 == 1
    x = INSIDE_X[left] if inside else OUTSIDE_X[left]
    return _pct(x, ys[(seat - 1) // 2])
 
 
def table_spot(table_num):
    label = TABLE_LABELS.get(table_num)
    return _pct(*label) if label else None
 
 
def chita(request):
    tables = SeatingTable.objects.prefetch_related('guests').all()
    query = request.GET.get('q', '').strip()
    found_table = None
    found_guest = None
 
    if query:
        for table in tables:
            for guest in table.guests.all():
                if query.lower() in guest.name.lower():
                    found_table = table
                    found_guest = guest
                    break
            if found_table:
                break
 
    spot = None
    if found_table:
        digits = ''.join(c for c in found_table.name.split()[0] if c.isdigit())
        if digits:
            num = int(digits)
            spot = seat_spot(num, found_guest.seat) or table_spot(num)
 
    guest_names = sorted(g.name for t in tables for g in t.guests.all())
 
    return render(request, 'envite/chita.html', {
        'guest_names': guest_names,
        'tables': tables,
        'query': query,
        'found_table': found_table,
        'found_guest': found_guest,
        'spot': spot,
    })
