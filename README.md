# FSX Navaids Update for NZ
Up-to-date navaids for NZ in Flight Simulator X.

Uses data from https://github.com/vatnz-dev/new-zealand-dataset to generate FSX-compatible XML with new navdata.

This update is available under the MIT License with Speed Restrictions exception. For more details on the Speed Restrictions exception, please read the LICENSE file.

## Currently supported
[x] Intersections (some bugs still)

[] VORs and NDBs (will be easy, when I figure out how it works)

[] Airways (no clue how this works)

## Usage
- Download the file "Airspace.xml" from https://github.com/vatnz-dev/new-zealand-dataset and place it in the same folder as this one.
- Install the FSX SDK. If you have a retail version of FSX, it should be included in the files. If you have FSX: Steam Edition, the required SDK files (specifically bglcomp.exe) is not included in the game files and you must use the [Prepar3D v1.4 SDK (direct download link)](https://cloud.prepar3d.com/SDK/Prepar3D_SDK_1.4.4747.0.exe).
- Edit "make.bat" and replace the path in "set bglcomp=..." to the path to "bglcomp.exe" in your SDK files (usually under "Environment SDK" and "BGL Compiler SDK". If it's missing, then you're trying to use the FSX Steam Edition SDK, which does not include it for licensing reasons apparently.)
- Run "make.bat" and copy "update.BGL" to FSX/Addon Scenery/scenery, and open the game.