# Euler Angle Interpolation (ZXZ / Vector Interpolation)

This script demonstrates simple **linear interpolation of Euler angles** between a start and end orientation. It works with Euler angles represented as 3‑element vectors and linearly interpolates them component‑wise.

A helper function for constructing a rotation matrix from **ZXZ Euler angles** is also provided, although the interpolation itself is performed directly in angle space (not via matrices or quaternions).

## Description

The script:

1. Defines rotation matrices for rotations about the X, Y, and Z axes.
2. Defines a function to build a rotation matrix from **ZXZ Euler angles** `[φ, θ, ψ]` (not used directly in the interpolation step, but useful for extension).
3. Converts between degrees and radians.
4. Prints Euler angles in a readable format.
5. Performs **linear interpolation** between two Euler angle vectors:
   - Start attitude `attitude0`
   - End attitude `attitude1`
   - Interpolation factor `t` in `[0, 1]`
6. Prints the start, end, and interpolated Euler angles (in degrees).

**Note:** Linear interpolation of Euler angles is simple but not always geometrically correct on the rotation manifold; it may not follow the shortest path on the sphere of orientations. For smoother, more correct interpolation, quaternions and slerp are typically used. This script is intentionally simple and illustrative.

## Requirements

- Python 3.x
- NumPy

To install NumPy:

`pip install numpy`

## Main Functions

- `rotationX(theta)`  
  Returns a 3×3 rotation matrix for a rotation about the X‑axis by angle `theta` (radians).

- `rotationY(theta)`  
  Returns a 3×3 rotation matrix for a rotation about the Y‑axis by angle `theta` (radians).

- `rotationZ(theta)`  
  Returns a 3×3 rotation matrix for a rotation about the Z‑axis by angle `theta` (radians).

- `rotationEulerZXZ(attitude_zxz)`  
  Builds a rotation matrix from ZXZ Euler angles `[φ, θ, ψ]` in radians using the sequence `Rz(φ) * Rx(θ) * Rz(ψ)`.  
  (Defined for completeness; not directly used for interpolation in the current script.)

- `radToDeg(rad)` / `degToRad(deg)`  
  Convert between radians and degrees. Work on scalars, lists, or NumPy arrays.

- `printEulerAngles(title, attitude_deg)`  
  Print Euler angles (in degrees) with a label, in the form:  
  `Euler Angles <Title> [phi, theta, psi]`.

- `linearInterpolate(v0, v1, t)`  
  Linearly interpolate between two vectors `v0` and `v1` using:  
  `v(t) = (1 − t) * v0 + t * v1`  
  Here, used to interpolate Euler angle vectors component‑wise.

## Default Example

The default start and end attitudes (in degrees) are:

- Start: `attitude0 = [0, 0, 0]`
- End: `attitude1 = [-30, 45, 135]`

They are converted to radians internally using `degToRad`.

The interpolation factor is:

- `t = 0.5` (mid‑point interpolation)

The script prints:

- Start Euler angles (deg)
- End Euler angles (deg)
- Interpolated Euler angles (deg)

## Customizing the Interpolation

You can change the **start and end Euler angles** easily:

- To set a different start attitude in degrees:

  `attitude0 = degToRad([phi0_deg, theta0_deg, psi0_deg])`

- To set a different end attitude in degrees:

  `attitude1 = degToRad([phi1_deg, theta1_deg, psi1_deg])`

You can also change the **interpolation parameter**:

- `t` should be between `0` and `1`:
  - `t = 0` gives the start attitude.
  - `t = 1` gives the end attitude.
  - Values in between give intermediate interpolated attitudes.

  Example:

  `t = 0.25` or `t = 0.75` for other intermediate points.

## Usage

1. Save the script to a file, for example: `euler_interpolation.py`.
2. Optionally edit:
   - `attitude0` and `attitude1` to set your desired start and end Euler angles (in degrees).
   - `t` to select the interpolation fraction.
3. Run the script:

   `python euler_interpolation.py`

4. Observe the printed start, end, and interpolated Euler angles in degrees.

## Notes and Limitations

- All internal trigonometric operations use **radians**; user‑facing values can be given in or converted to degrees.
- Interpolation here is **component‑wise linear in Euler angle space**, not on the rotation group SO(3); for some angle ranges this can cause:
  - Non‑minimal rotation paths.
  - Discontinuities around ±180°.
- For applications requiring smooth and geometrically correct interpolation between orientations, consider:
  - Converting Euler angles to quaternions.
  - Using quaternion slerp (spherical linear interpolation).
