module

public import Mathlib.Computability.TuringMachine.Computable

@[expose] public section

namespace ThreeSatRectilinearPictureCompression

/-- Q001's self-delimiting binary natural; length is logarithmic, not unary. -/
def encodeNat (n : Nat) : List Bool :=
  let bits := (Nat.toDigits 2 n).map (fun c => c == '1')
  List.replicate bits.length true ++ [false] ++ bits

def encodeList {α : Type} (encode : α → List Bool) (xs : List α) : List Bool :=
  encodeNat xs.length ++ xs.flatMap encode

def encodeOption {α : Type} (encode : α → List Bool) : Option α → List Bool
  | none => [false]
  | some x => true :: encode x

/-- None denotes mathematical nonexistence, never an execution error. -/
def searchOutput {I W : Type} (legal : I → Bool) (witness : I → W → Bool)
    (x : I) : Option W → Prop
  | some w => legal x = true ∧ witness x w = true
  | none => legal x = true ∧ ¬ ∃ w, witness x w = true

structure Formula where
  n : Nat
  clauses : List (List (Nat × Bool))
  deriving Repr

def legalSource (x : Formula) : Bool :=
  x.clauses.all (fun c => c.length == 3 && c.all (fun l => l.1 < x.n))

def sourceWitness (x : Formula) (a : List Bool) : Bool :=
  a.length == x.n && x.clauses.all (fun c => c.any (fun l => a[l.1]? == some l.2))

def encodeSource (x : Formula) : List Bool :=
  encodeNat x.n ++ encodeList (encodeList (fun l => encodeNat l.1 ++ [l.2])) x.clauses

def validSourceOutput := searchOutput legalSource sourceWitness

abbrev Instance := List (List Bool) × Nat
abbrev Rectangle := Nat × Nat × Nat × Nat
def legalTarget (x : Instance) : Bool :=
  x.1.all (fun row => row.length == (x.1.headD []).length)
def covers (r : Rectangle) (i j : Nat) : Bool :=
  r.1 ≤ i && i ≤ r.2.1 && r.2.2.1 ≤ j && j ≤ r.2.2.2
def targetWitness (x : Instance) (rects : List Rectangle) : Bool :=
  rects.length ≤ x.2 && rects.all (fun r =>
    r.1 ≤ r.2.1 && r.2.1 < x.1.length && r.2.2.1 ≤ r.2.2.2 && r.2.2.2 < (x.1.headD []).length) &&
  (List.range x.1.length).all (fun i => (List.range (x.1.headD []).length).all (fun j =>
    (rects.any (fun r => covers r i j)) == ((x.1[i]?.getD [])[j]?.getD false)))
def encodeTarget (x : Instance) := encodeList (encodeList (fun b => [b])) x.1 ++ encodeNat x.2
def encodeWitness := encodeList (fun r : Rectangle =>
  encodeNat r.1 ++ encodeNat r.2.1 ++ encodeNat r.2.2.1 ++ encodeNat r.2.2.2)
def validTargetOutput := searchOutput legalTarget targetWitness

/-- Both algorithms use Q001's explicit bit encoding and TM2 cost model.
Recovery receives the full pair of source instance and target output. -/
def Reduction (forward : Formula → Instance)
    (recover : Formula × Option (List Rectangle) → Option (List Bool)) : Prop :=
  Nonempty (Turing.TM2ComputableInPolyTime encodeSource encodeTarget forward) ∧
  Nonempty (Turing.TM2ComputableInPolyTime
    (fun input => encodeSource input.1 ++ (encodeOption encodeWitness) input.2)
    (encodeOption (encodeList (fun b => [b]))) recover) ∧
  (∃ bound : Polynomial Nat, ∀ x,
    (encodeTarget (forward x)).length ≤ bound.eval (encodeSource x).length) ∧
  (∃ bound : Polynomial Nat, ∀ input,
    ((encodeOption (encodeList (fun b => [b]))) (recover input)).length ≤
      bound.eval (encodeSource input.1 ++ (encodeOption encodeWitness) input.2).length) ∧
  (∀ x, legalSource x = true → legalTarget (forward x) = true) ∧
  (∀ x, legalSource x = true → ∀ y, validTargetOutput (forward x) y →
    validSourceOutput x (recover (x, y)))

def Goal : Prop :=
  ∃ (forward : Formula → Instance)
    (recover : Formula × Option (List Rectangle) → Option (List Bool)), Reduction forward recover

/-- Open question only; this placeholder is not a solution. -/
theorem solve : Goal := by
  sorry

end ThreeSatRectilinearPictureCompression
