import Challenge
open ThreeSatRectilinearPictureCompression
example : targetWitness ([[true,false],[true,true]], 1) [(0,1,0,1)] = false := by native_decide
example : targetWitness ([[true,false],[true,true]], 2) [(0,1,0,0),(1,1,0,1)] = true := by native_decide
