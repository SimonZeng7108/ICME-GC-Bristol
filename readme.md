# ICME 2025 Generalizable HDR & SDR Video Quality Measurement Grand Challenge
## Team Bristol - Chen Feng, Chengxi Zeng, Yuxuan Jiang, Robbie Hamilton, Tianhao Peng, Fan Zhang

## Overview
This repository contains code and resources for the ICME 2025 Grand Challenge focused on Generalizable HDR & SDR Video Quality Measurement. The challenge aims to improve objective video quality models (VQM) for both HDR (High Dynamic Range) and SDR (Standard Dynamic Range) video content.

## Benchmark

| Model      | PLCC  | SRCC  | KROCC |
|------------|-------|-------|-------|
| **Full-Reference (FR)** |       |       |       |
| PSNR       | 0.606 | 0.619 | 0.440 |
| VMAF       | 0.769 | 0.784 | 0.557 |
| MS-SSIM    | 0.634 | 0.640 | 0.457 |
| RankDVQA   | 0.614 | 0.624 |     x |
|------------|-------|-------|-------|
| **No-Reference (NR)**   |       |       |       |
| FastVQA    | 0.200 | 0.192 | 0.126 |
| COVER      | 0.433 | 0.430 | 0.290 |
| P1204.3    | 0.794 | 0.814 | 0.604 |
| HDRMAX     | TBD   | TBD   | TBD   |
| HDR-ChipQA | TBD   | TBD   | TBD   |
| Q-Align    | TBD   | TBD   | TBD   |
| Compression_RQ | TBD | TBD | TBD   |
| TVQA-C     | TBD   | TBD   | TBD   |

### FR
- [x] PSNR
- [x] VMAF
- [x] MS-SSIM
- [x] RankDVQA
- [ ] HDR-VDP-2.3

### NR
- [x] P1204.3
- [x] FastVQA
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