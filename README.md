# AMRadio
An AM Radio build with antenna design models, BOM, and schematic.
<p align="center">
 <img src="https://github.com/estods3/AMRadio/blob/main/radioisometric.jpg" alt="drawing" width="250"/>
 <img src="https://github.com/estods3/AMRadio/blob/main/radiowithearbuds.jpg" alt="drawing" width="140"/>
</p>

## Antenna Design
This section describes the criteria and techniques used to determine an antenna design for the radio.

### Criteria
* Medium Wave (MV) AM Radio. Frequency Range: 525kHz - 1600kHz.

* Using an AM "Loopstick" antenna consisting of a 140mm x 10mm cylindrical ferrite rod and 
  0-200pF variable air-gap capacitor + fixed 56pF ceramic capacitor in parallel (C=256pF).
  
* 10 "taps" in the coil using a 10-position rotary switch. 

* 9V operating voltage (used in amplifier).

### Results
Based on the design criteria above, here is the produced antenna design.

#### Frequency Heatmap
Determine the combinations of L and C that produce frequencies in the desired range. In this case, the MW AM spectrum.
<img src="https://github.com/estods3/AMRadio/blob/main/Radio1:%20AM%20Radio%20Germanium%20Diode/loopstick_frequency_LC_design.png" title="LC Tank Design" alt="drawing" width="500"/>

This heatmap can be produced using the model scripts/LCplotter.py.

Calculator: https://goodcalculators.com/resonant-frequency-calculator/

Radio Finder: https://radio-locator.com/

#### 400uH Inductive Coil
The inductance range needed for the coil was 150 - 400uH. The coil needs to have taps to allow the user to tune their radio to a desired resonance frequency. Here. 10 positions are used to cover from 150 to 400uH, as evenly spaced as possible. This is shown in the new heatmap below.

<img src="https://github.com/estods3/AMRadio/blob/main/Radio1:%20AM%20Radio%20Germanium%20Diode/LC_tap_design.png" title="LC Tap Design" alt="drawing" width="500"/>

The capacitor can be varied freely at each tap position to fine tune the resonance frequency

This heatmap can be produced using the model scripts/LCplotter.py.

Length: 

Diameter: 10mm

Number of Turns:


#### 56pF-256pF variable capacitor
A 56pF ceramic capacitor in parallel with a 250pF variable air-gap capacitor.

## Schematic
 2 Stage AM Radio consisting of AM Loopstick antenna (Design Above), Stage 1 Demodulation Circuit, Stage 2 Amplification Circuit, and Output Connector to 3.5mm audio jack.

<img src="https://github.com/estods3/AMRadio/blob/main/Radio1:%20AM%20Radio%20Germanium%20Diode/schematic_screenshot.png" title="AM Radio 1 Scematic" alt="drawing" width="1000"/>

## Bill of Materials

Materials used to make this project.

### AM Loopstick

antenna, coil, and tuning capacitor

* 140mm by 10mm (diameter) ferrite rod

* 1 roll of Magnet Wire

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
