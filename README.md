# Entry variables
- n = 10   # number of harmonics
- w = 900  # the highest frequency
- N = 256  # number of signals

# Plots
1. Rxx
2. Random y signal
3. Rxy

Щоб порівняти Rxx та Rxy при N = 10 та N = 1000, було обраховано середнє значення при повторних запусках програми. При цьому час виконання обрахунків приблизно однаковий, не залежить від N. Отримані середні результати:

# N = 10
- Rxx = 0.0770618625183144
- Rxy = 0.609398109469966
- Time Rxx = 0.014944600000000197
- Time Rxy = 1.8184589000000004

# N = 1000
- Rxx = 107.0214498532627
- Rxy = -104.92715662421897
- Time Rxx = 0.013572200000000034
- Time Rxy = 1.9052008999999996
