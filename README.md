# AMRadio
An AM Radio build with BOM and schematic
<p align="center">
 <img src="https://github.com/estods3/AMRadio/blob/main/radioisometric.jpg" alt="drawing" width="500"/>
 <img src="https://github.com/estods3/AMRadio/blob/main/radiowithearbuds.jpg" alt="drawing" width="281"/>
</p>

## Design
### Criteria
* Medium Wave (MV) AM Radio. Frequency Range: 525kHz - 1600kHz

* Using an AM "Loopstick" antenna consisting of a 140mm x 10mm cylindrical ferrite rod and 
  0-200pF variable air-gap capacitor + fixed 50pF ceramic capacitor in parallel (C=250pF).

* 9V operating voltage

### Results

#### Frequency Heatmap
Determine the combinations of L and C that produce frequencies in the desired range. In this case, the MW AM spectrum.
[<img src="https://github.com/estods3/AMRadio/blob/main/Radio1:%20AM%20Radio%20Germanium%20Diode/loopstick_frequency_LC_design.png" title="LC Tank Design" alt="drawing" width="200"/>]

Calculate a frequency table. For each desired frequency, compute what the needed inductance and capacitance.

Calculator: https://goodcalculators.com/resonant-frequency-calculator/

| Frequency (kHz) | Inductance (uH) | Capacitance (pF) |
| ----------- | ----------- | ----------- |
| 500      |    405     |    250   |
| 600      |    281     |    250   |
| 700      |    206     |    250   |
| 800      |    158     |    250   |
| 900      |    156     |    200   |
| 1000      |    126     |    200   |
| 1100      |    105     |    200   |
| 1200      |    88    |    200   |
| 1300      |    75     |    200   |
| 1400      |    126     |    100   |
| 1500      |    113     |    100   |
| 1600      |    200     |    50   |

#### 405uH Inductive Coil
Length: 

Diameter: 10mm

Number of Turns:


#### 50pF-250pF variable capacitor

## Schematic
 2 Stage AM Radio consisting of AM Loopstick antenna (Design Above), Stage 1 Demodulation Circuit, Stage 2 Amplification Circuit, and Output Connector to 3.5mm audio jack.

[<img src="https://github.com/estods3/AMRadio/blob/main/Radio1:%20AM%20Radio%20Germanium%20Diode/schematic_screenshot.png" title="AM Radio 1 Scematic" alt="drawing" width="200"/>]

## BOM

Materials used to make this project.

<p align="center">
 <img src="https://github.com/estods3/AMRadio/blob/main/radiotopdown.jpg" alt="drawing" width="500"/>
</p>

### AM Loopstick 

antenna, coil, and tuning capacitor

* 140mm by 10mm (diameter) ferrite rod

* 1 roll of Magnet Wire

* 1 365pF variable capacitor (air gap capacitor)

### Circuit
* 1 1N34 Germanium Diode

* Electrolytic Capacitor

* Ceramic Capacitors

### Output Stage
NOTE: For this project, an 8 ohm impedance output was desired (to use with modern earbuds). To use a high Z crystal radio ear piece, an output stage is likely not needed.
* 1 audio jack

* 1 audio amplifier chip

### Enclosure

Just for decorative purposes

* Balsa wood

* Natural Wood Stain

## Resources
http://techlib.com/electronics/crystal.html
http://radio-timetraveller.blogspot.com/2011/01/unassuming-antenna-ferrite-loopstick.html
https://radio-locator.com/
https://goodcalculators.com/resonant-frequency-calculator/
https://www.petervis.com/Radios/ferrite-rod-antenna-coil/calculator-for-mw-radio-coil.html
https://coil32.net/online-calculators/ferrite-rod-calculator.html
