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

# Positions are measured on the floor plan image (362 x 717 reference size)
# and converted to percentages, so they scale with the image.
IMG_W, IMG_H = 362, 717
 
# Fallback: marker at the table's label (x, y in reference pixels)
TABLE_LABELS = {
    0: (183, 70), 1: (282, 625), 2: (62, 625), 3: (225, 470), 4: (123, 470),
    5: (275, 320), 6: (62, 320), 7: (210, 205), 8: (123, 205),
    9: (285, 100), 10: (62, 100),
}
 
# Per table: y of first chair, spacing between chairs, chairs per side.
# Seats count from the end nearest the head table:
#   1 = inside #1, 2 = outside #1, 3 = inside #2, 4 = outside #2 ...
SHORT = {'first_y': 62.5, 'spacing': 17.5, 'per_side': 5}          # tables 10, 9
LONG_START = {8: 145.7, 7: 145.7, 6: 279, 5: 279,
              4: 412.3, 3: 412.3, 2: 545.7, 1: 545.7}
TABLES = {10: SHORT, 9: SHORT}
for _n, _start in LONG_START.items():
    TABLES[_n] = {'first_y': _start + 9.5, 'spacing': 16.2, 'per_side': 8}
 
LEFT_TABLES = {10, 8, 6, 4, 2}
INSIDE_X = {True: 106, False: 234}    # left-column tables / right-column tables
OUTSIDE_X = {True: 79.5, False: 260}
 
 
def _pct(x, y):
    return (round(x / IMG_W * 100, 1), round(y / IMG_H * 100, 1))
 
 
def seat_spot(table_num, seat):
    """Return (x%, y%) for a table number and seat number, or None."""
    t = TABLES.get(table_num)
    if not t or not seat or not 1 <= seat <= 2 * t['per_side']:
        return None
    left = table_num in LEFT_TABLES
    inside = seat % 2 == 1
    index = (seat - 1) // 2
    x = INSIDE_X[left] if inside else OUTSIDE_X[left]
    y = t['first_y'] + index * t['spacing']
    return _pct(x, y)
 
 
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
