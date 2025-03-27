# ICME 2025 Generalizable HDR & SDR Video Quality Measurement Grand Challenge
## Team Bristol - Chen Feng, Chengxi Zeng, Yuxuan Jiang, Robbie Hamilton, Fan Zhang

## Overview
This repository contains code and resources for the ICME 2025 Grand Challenge focused on Generalizable HDR & SDR Video Quality Measurement. The challenge aims to improve objective video quality models (VQM) for both HDR (High Dynamic Range) and SDR (Standard Dynamic Range) video content.

## Benchmark

| Model      | PLCC  | SRCC  | KROCC |
|------------|-------|-------|-------|
| **Full-Reference (FR)** |       |       |       |
| PSNR       | 0.606 | 0.619 | 0.440 |
| VMAF       | 0.769 | 0.784 | 0.557 |
| MS-SSIM    | 0.634 | 0.640 | 0.457 |
|------------|-------|-------|-------|
| **No-Reference (NR)**   |       |       |       |
| FastVQA    | TBD   | TBD   | TBD   |
| COVER      | 0.381 | 0.371 | 0.254 |
| P1204.3    | TBD   |       |       |
| HDRMAX     | TBD   | TBD   | TBD   |
| HDR-ChipQA | TBD   | TBD   | TBD   |
| Q-Align    | TBD   | TBD   | TBD   |
| Compression_RQ | TBD | TBD | TBD   |
| TVQA-C     | TBD   | TBD   | TBD   |

### FR
- [x] PSNR
- [x] VMAF
- [x] MS-SSIM
- [ ] HDR-VDP-3

### NR
- [ ] P1204.3
- [ ] FastVQA
- [x] COVER
- [ ] HDRMAX
- [ ] HDR-ChipQA
- [ ] Q-Align
- [ ] Compression_RQ
- [ ] TVQA-C

## Resources
For more information about the challenge, please visit the official [ICME 2025 Grand Challenge website](https://sites.google.com/view/icme25-vqm-gc/home?authuser=0).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.