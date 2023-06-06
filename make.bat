@echo off

set bglcomp="C:\Program Files (x86)\Lockheed Martin\Prepar3D SDK 1.4.4747.0\Environment Kit\BGL Compiler SDK\bglcomp.exe"

python generate_fixes.py
%bglcomp% update.xml || echo "An error occured while compiling!"