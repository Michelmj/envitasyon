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

# Fallback: marker at the table's label (x%, y%) on floorplan.jpg
TABLE_SPOTS = {
    0: (48, 4), 1: (81, 86), 2: (18, 85), 3: (63.5, 68), 4: (35, 68),
    5: (81, 49), 6: (18, 50.5), 7: (63.5, 32.5), 8: (35, 32),
    9: (80.5, 16), 10: (18, 14.8),
}

# Seat layout, in floorplan.jpg coordinates (image is ~1000 x 2000 units).
# Each long table has 8 chairs per side. Seats count from the end nearest
# the head table:  1 = inside #1, 2 = outside #1, 3 = inside #2, 4 = outside #2 ...
TABLE_START_Y = {10: 302, 9: 302, 8: 480, 7: 480, 6: 835, 5: 835,
                 4: 1187, 3: 1187, 2: 1545, 1: 1545}
# Chairs per side (default 8). Tables 10 and 9 are now a single short table.
CHAIRS_PER_SIDE = {10: 4, 9: 4}
LEFT_TABLES = {10, 8, 6, 4, 2}
INSIDE_X = {True: 307, False: 692}    # left-column tables / right-column tables
OUTSIDE_X = {True: 242, False: 757}
FIRST_CHAIR_OFFSET = 24     # distance from table start to first chair
CHAIR_SPACING = 43.6        # distance between chairs


def seat_spot(table_num, seat):
    """Return (x%, y%) for a table number and seat 1-16, or None."""
    max_seat = 2 * CHAIRS_PER_SIDE.get(table_num, 8)
    if table_num not in TABLE_START_Y or not seat or not 1 <= seat <= max_seat:
        return None
    left = table_num in LEFT_TABLES
    inside = seat % 2 == 1
    index = (seat - 1) // 2
    x = INSIDE_X[left] if inside else OUTSIDE_X[left]
    y = TABLE_START_Y[table_num] + FIRST_CHAIR_OFFSET + index * CHAIR_SPACING
    return (round(x / 10, 1), round(y / 20, 1))


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
            spot = seat_spot(num, found_guest.seat) or TABLE_SPOTS.get(num)

    guest_names = sorted(g.name for t in tables for g in t.guests.all())

    return render(request, 'envite/chita.html', {
        'guest_names': guest_names,
        'tables': tables,
        'query': query,
        'found_table': found_table,
        'found_guest': found_guest,
        'spot': spot,
    })
