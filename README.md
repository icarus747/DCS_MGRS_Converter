# DCS_MGRS_Converter
Simple MGRS grid converter to latitude longitude in degree decimal minute.

* Use by running the script and giving the MGRS location of interest.
  * First enter the Grid Zone. ie: 38T
  * Second enter the Square ID. ie: KN
  * Third enter the East-West position of at least 3 digits.
  * Forth enter the North-South position of at least 3 digits.
  * 38TKN732621

# TODO:
- Expand Converter to handle more than Caucasus and Persian Gulf Maps. (Hardcoded N/E Currently)
    - Write tests to confirm those
- Input Logic flexibility and Error Handling (Should take any format and spit out what is requested)
- Output to all other formats. (With filters for those who only want in 1 format)
- Keep code legible and maintainable. (Ongoing Reminder)