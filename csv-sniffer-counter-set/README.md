# Results

| Benchmark                                                                                                 | main    | csv-sniffer-counter-set |
|-----------------------------------------------------------------------------------------------------------|:-------:|:-----------------------:|
| csv_sniff(narrow.csv, 1024)                                                                               | 87.5 us | 31.6 us: 2.77x faster   |
| csv_sniff(narrow.csv, 2048)                                                                               | 132 us  | 52.9 us: 2.49x faster   |
| csv_sniff(narrow.csv, 4096)                                                                               | 220 us  | 96.2 us: 2.29x faster   |
| csv_sniff(ministers-overseas-travel-jan-mar-2013.csv, 1024)                                               | 346 us  | 286 us: 1.21x faster    |
| csv_sniff(ministers-overseas-travel-jan-mar-2013.csv, 2048)                                               | 362 us  | 293 us: 1.23x faster    |
| csv_sniff(ministers-overseas-travel-jan-mar-2013.csv, 4096)                                               | 362 us  | 293 us: 1.23x faster    |
| csv_sniff(Multiple commas in fields.csv, 1024)                                                            | 129 us  | 58.1 us: 2.22x faster   |
| csv_sniff(Multiple commas in fields.csv, 2048)                                                            | 129 us  | 58.0 us: 2.23x faster   |
| csv_sniff(Multiple commas in fields.csv, 4096)                                                            | 129 us  | 58.2 us: 2.22x faster   |
| csv_sniff(file_multitable_same.csv, 1024)                                                                 | 194 us  | 195 us: 1.00x slower    |
| csv_sniff(file_multitable_same.csv, 2048)                                                                 | 291 us  | 267 us: 1.09x faster    |
| csv_sniff(file_multitable_same.csv, 4096)                                                                 | 576 us  | 523 us: 1.10x faster    |
| csv_sniff(Line feed character is more frequent than the car return-line feed combination.csv, 1024)       | 208 us  | 169 us: 1.23x faster    |
| csv_sniff(Line feed character is more frequent than the car return-line feed combination.csv, 2048)       | 208 us  | 169 us: 1.23x faster    |
| csv_sniff(Line feed character is more frequent than the car return-line feed combination.csv, 4096)       | 208 us  | 169 us: 1.23x faster    |
| csv_sniff(wairakite-dh.csv, 1024)                                                                         | 178 us  | 63.9 us: 2.79x faster   |
| csv_sniff(wairakite-dh.csv, 2048)                                                                         | 179 us  | 64.0 us: 2.80x faster   |
| csv_sniff(wairakite-dh.csv, 4096)                                                                         | 179 us  | 63.9 us: 2.80x faster   |
| csv_sniff(1% nano+20% micro.csv, 1024)                                                                    | 568 us  | 232 us: 2.45x faster    |
| csv_sniff(1% nano+20% micro.csv, 2048)                                                                    | 570 us  | 235 us: 2.43x faster    |
| csv_sniff(1% nano+20% micro.csv, 4096)                                                                    | 575 us  | 238 us: 2.41x faster    |
| csv_sniff(air_quality_station3_2006.csv, 1024)                                                            | 180 us  | 72.3 us: 2.49x faster   |
| csv_sniff(air_quality_station3_2006.csv, 2048)                                                            | 182 us  | 73.9 us: 2.46x faster   |
| csv_sniff(air_quality_station3_2006.csv, 4096)                                                            | 185 us  | 77.1 us: 2.40x faster   |
| csv_sniff(Table embedded in the last record.csv, 1024)                                                    | 191 us  | 84.6 us: 2.26x faster   |
| csv_sniff(Table embedded in the last record.csv, 2048)                                                    | 191 us  | 84.8 us: 2.25x faster   |
| csv_sniff(Table embedded in the last record.csv, 4096)                                                    | 191 us  | 84.9 us: 2.25x faster   |
| csv_sniff(ResultsOR30x250-0.75_2.dat.csv, 1024)                                                           | 72.2 us | 30.5 us: 2.37x faster   |
| csv_sniff(ResultsOR30x250-0.75_2.dat.csv, 2048)                                                           | 135 us  | 92.4 us: 1.46x faster   |
| csv_sniff(ResultsOR30x250-0.75_2.dat.csv, 4096)                                                           | 224 us  | 169 us: 1.33x faster    |
| csv_sniff(file_no_trailing_newline.csv, 1024)                                                             | 194 us  | 195 us: 1.01x slower    |
| csv_sniff(file_no_trailing_newline.csv, 2048)                                                             | 291 us  | 269 us: 1.08x faster    |
| csv_sniff(file_no_trailing_newline.csv, 4096)                                                             | 579 us  | 525 us: 1.10x faster    |
| csv_sniff(csv_good_dialect_star.csv, 1024)                                                                | 856 us  | 421 us: 2.03x faster    |
| csv_sniff(csv_good_dialect_star.csv, 2048)                                                                | 1.72 ms | 773 us: 2.22x faster    |
| csv_sniff(csv_good_dialect_star.csv, 4096)                                                                | 3.43 ms | 1.52 ms: 2.26x faster   |
| csv_sniff(file_record_delimiter_0xD.csv, 1024)                                                            | 194 us  | 195 us: 1.01x slower    |
| csv_sniff(file_record_delimiter_0xD.csv, 2048)                                                            | 290 us  | 269 us: 1.08x faster    |
| csv_sniff(file_record_delimiter_0xD.csv, 4096)                                                            | 577 us  | 527 us: 1.09x faster    |
| csv_sniff(vissim_data_conf2473_i12_v2026.csv, 1024)                                                       | 203 us  | 105 us: 1.94x faster    |
| csv_sniff(vissim_data_conf2473_i12_v2026.csv, 2048)                                                       | 204 us  | 106 us: 1.93x faster    |
| csv_sniff(vissim_data_conf2473_i12_v2026.csv, 4096)                                                       | 207 us  | 107 us: 1.93x faster    |
| csv_sniff(file_quotation_char_0x27.csv, 1024)                                                             | 193 us  | 193 us: 1.00x faster    |
| csv_sniff(file_quotation_char_0x27.csv, 2048)                                                             | 289 us  | 266 us: 1.08x faster    |
| csv_sniff(file_quotation_char_0x27.csv, 4096)                                                             | 576 us  | 524 us: 1.10x faster    |
| csv_sniff(Note_4_Staff_costs_-_Average_number_of_persons_employed_13-14.csv, 1024)                        | 438 us  | 264 us: 1.66x faster    |
| csv_sniff(Note_4_Staff_costs_-_Average_number_of_persons_employed_13-14.csv, 2048)                        | 439 us  | 264 us: 1.66x faster    |
| csv_sniff(Note_4_Staff_costs_-_Average_number_of_persons_employed_13-14.csv, 4096)                        | 439 us  | 264 us: 1.67x faster    |
| csv_sniff(ResultsOR30x100-0.50_5.dat__m23.csv, 1024)                                                      | 105 us  | 76.0 us: 1.39x faster   |
| csv_sniff(ResultsOR30x100-0.50_5.dat__m23.csv, 2048)                                                      | 161 us  | 128 us: 1.26x faster    |
| csv_sniff(ResultsOR30x100-0.50_5.dat__m23.csv, 4096)                                                      | 268 us  | 206 us: 1.30x faster    |
| csv_sniff(ResultsOR30x100-0.50_10.dat__m28Infos.csv, 1024)                                                | 126 us  | 113 us: 1.11x faster    |
| csv_sniff(ResultsOR30x100-0.50_10.dat__m28Infos.csv, 2048)                                                | 126 us  | 113 us: 1.11x faster    |
| csv_sniff(ResultsOR30x100-0.50_10.dat__m28Infos.csv, 4096)                                                | 126 us  | 113 us: 1.11x faster    |
| csv_sniff(row_less_sep_row5_col6.csv, 1024)                                                               | 195 us  | 195 us: 1.00x slower    |
| csv_sniff(row_less_sep_row5_col6.csv, 2048)                                                               | 290 us  | 270 us: 1.08x faster    |
| csv_sniff(row_less_sep_row5_col6.csv, 4096)                                                               | 576 us  | 526 us: 1.09x faster    |
| csv_sniff(ResultsOR30x250-0.75_9.datInfos.csv, 1024)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.75_9.datInfos.csv, 2048)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.75_9.datInfos.csv, 4096)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(epcs-dwp-cmg-spend-july-2017.csv, 1024)                                                         | 1.07 ms | 568 us: 1.88x faster    |
| csv_sniff(epcs-dwp-cmg-spend-july-2017.csv, 2048)                                                         | 1.07 ms | 570 us: 1.87x faster    |
| csv_sniff(epcs-dwp-cmg-spend-july-2017.csv, 4096)                                                         | 1.07 ms | 571 us: 1.87x faster    |
| csv_sniff(ResultsOR30x250-0.75_4.datInfos.csv, 1024)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.75_4.datInfos.csv, 2048)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.75_4.datInfos.csv, 4096)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(erionite.csv, 1024)                                                                             | 177 us  | 62.1 us: 2.86x faster   |
| csv_sniff(erionite.csv, 2048)                                                                             | 177 us  | 62.2 us: 2.84x faster   |
| csv_sniff(erionite.csv, 4096)                                                                             | 178 us  | 62.0 us: 2.87x faster   |
| csv_sniff(ResultsOR30x100-0.25_5.dat__m28.csv, 1024)                                                      | 103 us  | 71.5 us: 1.45x faster   |
| csv_sniff(ResultsOR30x100-0.25_5.dat__m28.csv, 2048)                                                      | 159 us  | 122 us: 1.30x faster    |
| csv_sniff(ResultsOR30x100-0.25_5.dat__m28.csv, 4096)                                                      | 267 us  | 203 us: 1.31x faster    |
| csv_sniff(file_field_delimiter_0x20.csv, 1024)                                                            | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(file_field_delimiter_0x20.csv, 2048)                                                            | 289 us  | 268 us: 1.08x faster    |
| csv_sniff(file_field_delimiter_0x20.csv, 4096)                                                            | 574 us  | 526 us: 1.09x faster    |
| csv_sniff(W32.csv, 1024)                                                                                  | 186 us  | 79.0 us: 2.35x faster   |
| csv_sniff(W32.csv, 2048)                                                                                  | 188 us  | 81.2 us: 2.32x faster   |
| csv_sniff(W32.csv, 4096)                                                                                  | 191 us  | 84.6 us: 2.26x faster   |
| csv_sniff(Pipe character is more frequent than the semicolon.csv, 1024)                                   | 69.7 us | 74.7 us: 1.07x slower   |
| csv_sniff(Pipe character is more frequent than the semicolon.csv, 2048)                                   | 69.7 us | 74.9 us: 1.07x slower   |
| csv_sniff(Pipe character is more frequent than the semicolon.csv, 4096)                                   | 69.6 us | 74.8 us: 1.07x slower   |
| csv_sniff(ResultsOR30x100-0.50_1.dat__m21.csv, 1024)                                                      | 108 us  | 82.7 us: 1.31x faster   |
| csv_sniff(ResultsOR30x100-0.50_1.dat__m21.csv, 2048)                                                      | 161 us  | 128 us: 1.26x faster    |
| csv_sniff(ResultsOR30x100-0.50_1.dat__m21.csv, 4096)                                                      | 281 us  | 210 us: 1.34x faster    |
| csv_sniff(row_field_delimiter_0_0x20.csv, 1024)                                                           | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(row_field_delimiter_0_0x20.csv, 2048)                                                           | 290 us  | 269 us: 1.08x faster    |
| csv_sniff(row_field_delimiter_0_0x20.csv, 4096)                                                           | 575 us  | 526 us: 1.09x faster    |
| csv_sniff(file_one_data_row.csv, 1024)                                                                    | 98.7 us | 105 us: 1.06x slower    |
| csv_sniff(file_one_data_row.csv, 2048)                                                                    | 99.0 us | 105 us: 1.06x slower    |
| csv_sniff(file_one_data_row.csv, 4096)                                                                    | 98.7 us | 105 us: 1.07x slower    |
| csv_sniff(file_multitable_less.csv, 1024)                                                                 | 195 us  | 196 us: 1.00x slower    |
| csv_sniff(file_multitable_less.csv, 2048)                                                                 | 291 us  | 270 us: 1.08x faster    |
| csv_sniff(file_multitable_less.csv, 4096)                                                                 | 575 us  | 527 us: 1.09x faster    |
| csv_sniff(ResultsOR30x250-0.50_1.datInfos.csv, 1024)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.50_1.datInfos.csv, 2048)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(ResultsOR30x250-0.50_1.datInfos.csv, 4096)                                                      | 126 us  | 113 us: 1.12x faster    |
| csv_sniff(fr_hypo1.csv, 1024)                                                                             | 179 us  | 67.4 us: 2.65x faster   |
| csv_sniff(fr_hypo1.csv, 2048)                                                                             | 181 us  | 69.5 us: 2.60x faster   |
| csv_sniff(fr_hypo1.csv, 4096)                                                                             | 184 us  | 72.5 us: 2.53x faster   |
| csv_sniff(ResultsOR30x500-0.50_6.datInfos.csv, 1024)                                                      | 127 us  | 114 us: 1.11x faster    |
| csv_sniff(ResultsOR30x500-0.50_6.datInfos.csv, 2048)                                                      | 127 us  | 115 us: 1.11x faster    |
| csv_sniff(ResultsOR30x500-0.50_6.datInfos.csv, 4096)                                                      | 127 us  | 115 us: 1.11x faster    |
| csv_sniff(dwp-cmg-spend-1214.csv, 1024)                                                                   | 210 us  | 173 us: 1.21x faster    |
| csv_sniff(dwp-cmg-spend-1214.csv, 2048)                                                                   | 209 us  | 173 us: 1.21x faster    |
| csv_sniff(dwp-cmg-spend-1214.csv, 4096)                                                                   | 209 us  | 173 us: 1.21x faster    |
| csv_sniff(picasso.csv, 1024)                                                                              | 185 us  | 85.9 us: 2.16x faster   |
| csv_sniff(picasso.csv, 2048)                                                                              | 349 us  | 155 us: 2.25x faster    |
| csv_sniff(picasso.csv, 4096)                                                                              | 695 us  | 301 us: 2.31x faster    |
| csv_sniff(file_no_header.csv, 2048)                                                                       | 251 us  | 237 us: 1.06x faster    |
| csv_sniff(file_no_header.csv, 4096)                                                                       | 525 us  | 469 us: 1.12x faster    |
| csv_sniff(spending_2020_01.csv, 1024)                                                                     | 183 us  | 166 us: 1.10x faster    |
| csv_sniff(spending_2020_01.csv, 2048)                                                                     | 260 us  | 226 us: 1.15x faster    |
| csv_sniff(spending_2020_01.csv, 4096)                                                                     | 282 us  | 233 us: 1.21x faster    |
| csv_sniff(ResultsOR30x100-0.50_3.dat.csv, 1024)                                                           | 104 us  | 71.7 us: 1.45x faster   |
| csv_sniff(ResultsOR30x100-0.50_3.dat.csv, 2048)                                                           | 160 us  | 125 us: 1.28x faster    |
| csv_sniff(ResultsOR30x100-0.50_3.dat.csv, 4096)                                                           | 268 us  | 205 us: 1.31x faster    |
| csv_sniff(download (10).csv, 1024)                                                                        | 454 us  | 306 us: 1.48x faster    |
| csv_sniff(download (10).csv, 2048)                                                                        | 1.03 ms | 706 us: 1.46x faster    |
| csv_sniff(download (10).csv, 4096)                                                                        | 1.16 ms | 769 us: 1.51x faster    |
| csv_sniff(ResultsOR30x250-0.75_3.dat.csv, 1024)                                                           | 72.5 us | 30.4 us: 2.38x faster   |
| csv_sniff(ResultsOR30x250-0.75_3.dat.csv, 2048)                                                           | 136 us  | 92.7 us: 1.46x faster   |
| csv_sniff(ResultsOR30x250-0.75_3.dat.csv, 4096)                                                           | 225 us  | 169 us: 1.33x faster    |
| csv_sniff(business_expenses_apr_jun_14_peter_lewis.csv, 1024)                                             | 347 us  | 235 us: 1.47x faster    |
| csv_sniff(business_expenses_apr_jun_14_peter_lewis.csv, 2048)                                             | 347 us  | 236 us: 1.47x faster    |
| csv_sniff(business_expenses_apr_jun_14_peter_lewis.csv, 4096)                                             | 348 us  | 235 us: 1.48x faster    |
| csv_sniff(Mixed comma and colon - [clevercsv issue #35].csv, 1024)                                        | 353 us  | 167 us: 2.12x faster    |
| csv_sniff(Mixed comma and colon - [clevercsv issue #35].csv, 2048)                                        | 404 us  | 190 us: 2.12x faster    |
| csv_sniff(Mixed comma and colon - [clevercsv issue #35].csv, 4096)                                        | 404 us  | 191 us: 2.12x faster    |
| csv_sniff(LOS_1050CFit.csv, 1024)                                                                         | 464 us  | 198 us: 2.34x faster    |
| csv_sniff(LOS_1050CFit.csv, 2048)                                                                         | 853 us  | 337 us: 2.53x faster    |
| csv_sniff(LOS_1050CFit.csv, 4096)                                                                         | 1.63 ms | 620 us: 2.63x faster    |
| csv_sniff(file_header_multirow_2.csv, 1024)                                                               | 205 us  | 194 us: 1.05x faster    |
| csv_sniff(file_header_multirow_2.csv, 2048)                                                               | 285 us  | 262 us: 1.09x faster    |
| csv_sniff(file_header_multirow_2.csv, 4096)                                                               | 586 us  | 526 us: 1.11x faster    |
| csv_sniff(ResultsOR30x100-0.75_5.dat__m29Infos.csv, 1024)                                                 | 127 us  | 117 us: 1.09x faster    |
| csv_sniff(ResultsOR30x100-0.75_5.dat__m29Infos.csv, 2048)                                                 | 127 us  | 117 us: 1.09x faster    |
| csv_sniff(ResultsOR30x100-0.75_5.dat__m29Infos.csv, 4096)                                                 | 127 us  | 117 us: 1.09x faster    |
| csv_sniff(FEC data - [clevercsv issue #15].csv, 1024)                                                     | 134 us  | 96.1 us: 1.40x faster   |
| csv_sniff(FEC data - [clevercsv issue #15].csv, 2048)                                                     | 134 us  | 96.2 us: 1.39x faster   |
| csv_sniff(FEC data - [clevercsv issue #15].csv, 4096)                                                     | 134 us  | 95.9 us: 1.40x faster   |
| csv_sniff(Feb-2016.csv, 1024)                                                                             | 202 us  | 131 us: 1.54x faster    |
| csv_sniff(Feb-2016.csv, 2048)                                                                             | 203 us  | 131 us: 1.54x faster    |
| csv_sniff(Feb-2016.csv, 4096)                                                                             | 203 us  | 131 us: 1.55x faster    |
| csv_sniff(O18_air.csv, 1024)                                                                              | 178 us  | 61.2 us: 2.91x faster   |
| csv_sniff(O18_air.csv, 2048)                                                                              | 180 us  | 63.0 us: 2.85x faster   |
| csv_sniff(O18_air.csv, 4096)                                                                              | 183 us  | 65.6 us: 2.78x faster   |
| csv_sniff(nati-clin-audi-bowe-canc-2017-tran-main-fiel-list.csv, 1024)                                    | 177 us  | 146 us: 1.22x faster    |
| csv_sniff(nati-clin-audi-bowe-canc-2017-tran-main-fiel-list.csv, 2048)                                    | 247 us  | 208 us: 1.19x faster    |
| csv_sniff(nati-clin-audi-bowe-canc-2017-tran-main-fiel-list.csv, 4096)                                    | 1.02 ms | 735 us: 1.38x faster    |
| csv_sniff(moj-aramis-data-march-11.csv, 1024)                                                             | 261 us  | 235 us: 1.11x faster    |
| csv_sniff(moj-aramis-data-march-11.csv, 2048)                                                             | 514 us  | 443 us: 1.16x faster    |
| csv_sniff(moj-aramis-data-march-11.csv, 4096)                                                             | 802 us  | 683 us: 1.17x faster    |
| csv_sniff(fr_RG65_pageid.csv, 1024)                                                                       | 186 us  | 86.5 us: 2.16x faster   |
| csv_sniff(fr_RG65_pageid.csv, 2048)                                                                       | 187 us  | 86.7 us: 2.16x faster   |
| csv_sniff(fr_RG65_pageid.csv, 4096)                                                                       | 187 us  | 86.4 us: 2.16x faster   |
| csv_sniff(file_field_delimiter_0x9.csv, 1024)                                                             | 196 us  | 198 us: 1.01x slower    |
| csv_sniff(file_field_delimiter_0x9.csv, 2048)                                                             | 291 us  | 272 us: 1.07x faster    |
| csv_sniff(file_field_delimiter_0x9.csv, 4096)                                                             | 300 us  | 277 us: 1.08x faster    |
| csv_sniff(row_extra_quote0_col0.csv, 1024)                                                                | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(row_extra_quote0_col0.csv, 2048)                                                                | 290 us  | 268 us: 1.08x faster    |
| csv_sniff(row_extra_quote0_col0.csv, 4096)                                                                | 575 us  | 524 us: 1.10x faster    |
| csv_sniff(senior-staff-march-2020.csv, 2048)                                                              | 263 us  | 240 us: 1.10x faster    |
| csv_sniff(senior-staff-march-2020.csv, 4096)                                                              | 539 us  | 472 us: 1.14x faster    |
| csv_sniff(Json data type - [clevercsv issue #37].csv, 1024)                                               | 154 us  | 78.5 us: 1.97x faster   |
| csv_sniff(Json data type - [clevercsv issue #37].csv, 2048)                                               | 155 us  | 78.6 us: 1.97x faster   |
| csv_sniff(Json data type - [clevercsv issue #37].csv, 4096)                                               | 154 us  | 78.6 us: 1.97x faster   |
| csv_sniff(ResultsOR30x100-0.75_1.dat__m21Infos.csv, 1024)                                                 | 126 us  | 115 us: 1.10x faster    |
| csv_sniff(ResultsOR30x100-0.75_1.dat__m21Infos.csv, 2048)                                                 | 126 us  | 115 us: 1.10x faster    |
| csv_sniff(ResultsOR30x100-0.75_1.dat__m21Infos.csv, 4096)                                                 | 126 us  | 115 us: 1.10x faster    |
| csv_sniff(row_more_sep_row0_col0.csv, 1024)                                                               | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(row_more_sep_row0_col0.csv, 2048)                                                               | 290 us  | 270 us: 1.07x faster    |
| csv_sniff(row_more_sep_row0_col0.csv, 4096)                                                               | 575 us  | 526 us: 1.09x faster    |
| csv_sniff(Pipe character is more frequent than the comma.csv, 1024)                                       | 69.4 us | 74.7 us: 1.08x slower   |
| csv_sniff(Pipe character is more frequent than the comma.csv, 2048)                                       | 69.6 us | 74.9 us: 1.08x slower   |
| csv_sniff(Pipe character is more frequent than the comma.csv, 4096)                                       | 69.7 us | 74.8 us: 1.07x slower   |
| csv_sniff(public-toilet-borough-grid.csv, 1024)                                                           | 198 us  | 173 us: 1.15x faster    |
| csv_sniff(public-toilet-borough-grid.csv, 2048)                                                           | 269 us  | 231 us: 1.16x faster    |
| csv_sniff(public-toilet-borough-grid.csv, 4096)                                                           | 271 us  | 233 us: 1.17x faster    |
| csv_sniff(Copy_of_2016-17_Q3_Final_V2.csv, 1024)                                                          | 228 us  | 199 us: 1.15x faster    |
| csv_sniff(Copy_of_2016-17_Q3_Final_V2.csv, 2048)                                                          | 487 us  | 389 us: 1.25x faster    |
| csv_sniff(Copy_of_2016-17_Q3_Final_V2.csv, 4096)                                                          | 1.01 ms | 777 us: 1.30x faster    |
| csv_sniff(Optional quoted fields.csv, 1024)                                                               | 42.3 us | 15.2 us: 2.79x faster   |
| csv_sniff(Optional quoted fields.csv, 2048)                                                               | 42.3 us | 15.2 us: 2.78x faster   |
| csv_sniff(Optional quoted fields.csv, 4096)                                                               | 42.3 us | 15.1 us: 2.79x faster   |
| csv_sniff(2004-2016.csv, 1024)                                                                            | 194 us  | 97.3 us: 2.00x faster   |
| csv_sniff(2004-2016.csv, 2048)                                                                            | 196 us  | 98.8 us: 1.98x faster   |
| csv_sniff(2004-2016.csv, 4096)                                                                            | 199 us  | 101 us: 1.96x faster    |
| csv_sniff(SouthTrent_Demand_zone-based.csv, 1024)                                                         | 72.3 us | 32.5 us: 2.22x faster   |
| csv_sniff(SouthTrent_Demand_zone-based.csv, 2048)                                                         | 123 us  | 64.6 us: 1.91x faster   |
| csv_sniff(SouthTrent_Demand_zone-based.csv, 4096)                                                         | 204 us  | 124 us: 1.64x faster    |
| csv_sniff(dd_Wickenburg_nobmp_623.csv, 1024)                                                              | 317 us  | 209 us: 1.52x faster    |
| csv_sniff(dd_Wickenburg_nobmp_623.csv, 2048)                                                              | 376 us  | 265 us: 1.42x faster    |
| csv_sniff(dd_Wickenburg_nobmp_623.csv, 4096)                                                              | 439 us  | 311 us: 1.41x faster    |
| csv_sniff(Oct_2013.csv, 1024)                                                                             | 78.9 us | 79.1 us: 1.00x slower   |
| csv_sniff(Oct_2013.csv, 2048)                                                                             | 253 us  | 191 us: 1.33x faster    |
| csv_sniff(Oct_2013.csv, 4096)                                                                             | 672 us  | 457 us: 1.47x faster    |
| csv_sniff(file_double_trailing_newline.csv, 1024)                                                         | 195 us  | 196 us: 1.00x slower    |
| csv_sniff(file_double_trailing_newline.csv, 2048)                                                         | 290 us  | 269 us: 1.08x faster    |
| csv_sniff(file_double_trailing_newline.csv, 4096)                                                         | 576 us  | 527 us: 1.09x faster    |
| csv_sniff(ResultsOR30x100-0.25_10.dat__m21Infos.csv, 1024)                                                | 127 us  | 115 us: 1.10x faster    |
| csv_sniff(ResultsOR30x100-0.25_10.dat__m21Infos.csv, 2048)                                                | 127 us  | 116 us: 1.10x faster    |
| csv_sniff(ResultsOR30x100-0.25_10.dat__m21Infos.csv, 4096)                                                | 127 us  | 115 us: 1.10x faster    |
| csv_sniff(ministry-of-defence__30-09-2012__mod_300912-Air-Govt-data-template-u-senior.csv, 1024)          | 120 us  | 123 us: 1.02x slower    |
| csv_sniff(ministry-of-defence__30-09-2012__mod_300912-Air-Govt-data-template-u-senior.csv, 2048)          | 220 us  | 204 us: 1.08x faster    |
| csv_sniff(ministry-of-defence__30-09-2012__mod_300912-Air-Govt-data-template-u-senior.csv, 4096)          | 349 us  | 306 us: 1.14x faster    |
| csv_sniff(row_field_delimiter_5_0x20.csv, 1024)                                                           | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(row_field_delimiter_5_0x20.csv, 2048)                                                           | 291 us  | 270 us: 1.07x faster    |
| csv_sniff(row_field_delimiter_5_0x20.csv, 4096)                                                           | 577 us  | 529 us: 1.09x faster    |
| csv_sniff(GPC_DCLG_December_2015_for_Publication.csv, 1024)                                               | 200 us  | 209 us: 1.05x slower    |
| csv_sniff(GPC_DCLG_December_2015_for_Publication.csv, 2048)                                               | 288 us  | 276 us: 1.04x faster    |
| csv_sniff(GPC_DCLG_December_2015_for_Publication.csv, 4096)                                               | 288 us  | 276 us: 1.04x faster    |
| csv_sniff(HMRC_spending_over_25000_for_September_2018.csv, 1024)                                          | 220 us  | 207 us: 1.06x faster    |
| csv_sniff(HMRC_spending_over_25000_for_September_2018.csv, 2048)                                          | 453 us  | 408 us: 1.11x faster    |
| csv_sniff(HMRC_spending_over_25000_for_September_2018.csv, 4096)                                          | 783 us  | 686 us: 1.14x faster    |
| csv_sniff(permanent_secretary_and_director_general_expenses_and_hospitality_april_to_june_2012.csv, 1024) | 590 us  | 408 us: 1.45x faster    |
| csv_sniff(permanent_secretary_and_director_general_expenses_and_hospitality_april_to_june_2012.csv, 2048) | 1.29 ms | 814 us: 1.58x faster    |
| csv_sniff(permanent_secretary_and_director_general_expenses_and_hospitality_april_to_june_2012.csv, 4096) | 2.34 ms | 1.43 ms: 1.63x faster   |
| csv_sniff(planning-application-aug-17.csv, 1024)                                                          | 440 us  | 292 us: 1.51x faster    |
| csv_sniff(planning-application-aug-17.csv, 2048)                                                          | 1.12 ms | 695 us: 1.61x faster    |
| csv_sniff(planning-application-aug-17.csv, 4096)                                                          | 2.35 ms | 1.44 ms: 1.63x faster   |
| csv_sniff(mos-oct-dec-2014.csv, 1024)                                                                     | 200 us  | 114 us: 1.76x faster    |
| csv_sniff(mos-oct-dec-2014.csv, 2048)                                                                     | 201 us  | 115 us: 1.75x faster    |
| csv_sniff(mos-oct-dec-2014.csv, 4096)                                                                     | 203 us  | 117 us: 1.74x faster    |
| csv_sniff(April-2011-for-publication.csv, 1024)                                                           | 220 us  | 203 us: 1.08x faster    |
| csv_sniff(April-2011-for-publication.csv, 2048)                                                           | 439 us  | 381 us: 1.15x faster    |
| csv_sniff(April-2011-for-publication.csv, 4096)                                                           | 770 us  | 635 us: 1.21x faster    |
| csv_sniff(20170320-ePC_Data-Travel-Stationery.csv, 1024)                                                  | 202 us  | 125 us: 1.62x faster    |
| csv_sniff(20170320-ePC_Data-Travel-Stationery.csv, 2048)                                                  | 202 us  | 125 us: 1.62x faster    |
| csv_sniff(20170320-ePC_Data-Travel-Stationery.csv, 4096)                                                  | 202 us  | 125 us: 1.62x faster    |
| csv_sniff(Rainbow CSV [issue #92].csv, 1024)                                                              | 123 us  | 130 us: 1.06x slower    |
| csv_sniff(Rainbow CSV [issue #92].csv, 2048)                                                              | 125 us  | 132 us: 1.06x slower    |
| csv_sniff(Rainbow CSV [issue #92].csv, 4096)                                                              | 125 us  | 132 us: 1.06x slower    |
| csv_sniff(hypo5.csv, 1024)                                                                                | 181 us  | 71.4 us: 2.54x faster   |
| csv_sniff(hypo5.csv, 2048)                                                                                | 182 us  | 72.9 us: 2.50x faster   |
| csv_sniff(hypo5.csv, 4096)                                                                                | 185 us  | 75.4 us: 2.45x faster   |
| csv_sniff(S30out.csv, 1024)                                                                               | 74.3 us | 40.3 us: 1.84x faster   |
| csv_sniff(S30out.csv, 2048)                                                                               | 133 us  | 81.3 us: 1.64x faster   |
| csv_sniff(S30out.csv, 4096)                                                                               | 234 us  | 126 us: 1.86x faster    |
| csv_sniff(AL5083-emissivity.csv, 1024)                                                                    | 180 us  | 71.9 us: 2.50x faster   |
| csv_sniff(AL5083-emissivity.csv, 2048)                                                                    | 182 us  | 74.5 us: 2.45x faster   |
| csv_sniff(AL5083-emissivity.csv, 4096)                                                                    | 183 us  | 75.1 us: 2.44x faster   |
| csv_sniff(june_2015(1).csv, 1024)                                                                         | 228 us  | 198 us: 1.16x faster    |
| csv_sniff(june_2015(1).csv, 2048)                                                                         | 248 us  | 204 us: 1.22x faster    |
| csv_sniff(june_2015(1).csv, 4096)                                                                         | 249 us  | 205 us: 1.21x faster    |
| csv_sniff(Businesses with a rateable value of less than $12,000 - March 2016.csv, 1024)                   | 256 us  | 210 us: 1.22x faster    |
| csv_sniff(Businesses with a rateable value of less than $12,000 - March 2016.csv, 2048)                   | 498 us  | 411 us: 1.21x faster    |
| csv_sniff(Businesses with a rateable value of less than $12,000 - March 2016.csv, 4096)                   | 1.01 ms | 822 us: 1.23x faster    |
| csv_sniff(file_field_delimiter_0x2C_0x20.csv, 1024)                                                       | 195 us  | 195 us: 1.00x slower    |
| csv_sniff(file_field_delimiter_0x2C_0x20.csv, 2048)                                                       | 288 us  | 261 us: 1.10x faster    |
| csv_sniff(file_field_delimiter_0x2C_0x20.csv, 4096)                                                       | 577 us  | 521 us: 1.11x faster    |
| csv_sniff(Resultsgk06.datInfos.csv, 1024)                                                                 | 125 us  | 112 us: 1.12x faster    |
| csv_sniff(Resultsgk06.datInfos.csv, 2048)                                                                 | 125 us  | 112 us: 1.11x faster    |
| csv_sniff(Resultsgk06.datInfos.csv, 4096)                                                                 | 125 us  | 112 us: 1.11x faster    |
| csv_sniff(ResultsOR30x250-0.25_7.dat.csv, 1024)                                                           | 72.4 us | 30.6 us: 2.37x faster   |
| csv_sniff(ResultsOR30x250-0.25_7.dat.csv, 2048)                                                           | 136 us  | 92.8 us: 1.46x faster   |
| csv_sniff(ResultsOR30x250-0.25_7.dat.csv, 4096)                                                           | 224 us  | 169 us: 1.33x faster    |
| csv_sniff(file_escape_char_0x5C.csv, 1024)                                                                | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(file_escape_char_0x5C.csv, 2048)                                                                | 290 us  | 269 us: 1.08x faster    |
| csv_sniff(file_escape_char_0x5C.csv, 4096)                                                                | 575 us  | 527 us: 1.09x faster    |
| csv_sniff(file_escape_char_0x00.csv, 1024)                                                                | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(file_escape_char_0x00.csv, 2048)                                                                | 290 us  | 270 us: 1.07x faster    |
| csv_sniff(file_escape_char_0x00.csv, 4096)                                                                | 575 us  | 526 us: 1.09x faster    |
| csv_sniff(Kokad pollen.csv, 1024)                                                                         | 76.3 us | 60.8 us: 1.26x faster   |
| csv_sniff(Kokad pollen.csv, 2048)                                                                         | 111 us  | 93.2 us: 1.19x faster   |
| csv_sniff(Kokad pollen.csv, 4096)                                                                         | 274 us  | 211 us: 1.30x faster    |
| csv_sniff(Wakefield Council Procurement Card Transactions 2018-19 Q2.csv, 1024)                           | 206 us  | 199 us: 1.04x faster    |
| csv_sniff(Wakefield Council Procurement Card Transactions 2018-19 Q2.csv, 2048)                           | 276 us  | 247 us: 1.12x faster    |
| csv_sniff(Wakefield Council Procurement Card Transactions 2018-19 Q2.csv, 4096)                           | 277 us  | 250 us: 1.11x faster    |
| csv_sniff(File with multi-line field.csv, 1024)                                                           | 78.4 us | 28.7 us: 2.74x faster   |
| csv_sniff(File with multi-line field.csv, 2048)                                                           | 78.3 us | 28.7 us: 2.73x faster   |
| csv_sniff(File with multi-line field.csv, 4096)                                                           | 78.3 us | 28.7 us: 2.73x faster   |
| csv_sniff(file_preamble.csv, 1024)                                                                        | 217 us  | 199 us: 1.09x faster    |
| csv_sniff(file_preamble.csv, 2048)                                                                        | 409 us  | 381 us: 1.07x faster    |
| csv_sniff(file_preamble.csv, 4096)                                                                        | 599 us  | 530 us: 1.13x faster    |
| csv_sniff(student_loans_company_limited-2011-09-30-organogram-senior.csv, 1024)                           | 119 us  | 119 us: 1.00x faster    |
| csv_sniff(student_loans_company_limited-2011-09-30-organogram-senior.csv, 2048)                           | 210 us  | 210 us: 1.00x slower    |
| csv_sniff(student_loans_company_limited-2011-09-30-organogram-senior.csv, 4096)                           | 313 us  | 298 us: 1.05x faster    |
| csv_sniff(over25k-transparency.csv, 1024)                                                                 | 250 us  | 203 us: 1.23x faster    |
| csv_sniff(over25k-transparency.csv, 2048)                                                                 | 505 us  | 390 us: 1.30x faster    |
| csv_sniff(over25k-transparency.csv, 4096)                                                                 | 999 us  | 743 us: 1.34x faster    |
| csv_sniff(OccurrenceData351.csv, 1024)                                                                    | 523 us  | 245 us: 2.13x faster    |
| csv_sniff(OccurrenceData351.csv, 2048)                                                                    | 1.01 ms | 469 us: 2.15x faster    |
| csv_sniff(OccurrenceData351.csv, 4096)                                                                    | 2.00 ms | 926 us: 2.16x faster    |
| csv_sniff(Takakai2008-ch4.csv, 1024)                                                                      | 191 us  | 84.4 us: 2.27x faster   |
| csv_sniff(Takakai2008-ch4.csv, 2048)                                                                      | 191 us  | 84.6 us: 2.26x faster   |
| csv_sniff(Takakai2008-ch4.csv, 4096)                                                                      | 191 us  | 84.3 us: 2.27x faster   |
| csv_sniff(10.January_2019.csv, 1024)                                                                      | 230 us  | 204 us: 1.13x faster    |
| csv_sniff(10.January_2019.csv, 2048)                                                                      | 438 us  | 379 us: 1.16x faster    |
| csv_sniff(10.January_2019.csv, 4096)                                                                      | 789 us  | 637 us: 1.24x faster    |
| csv_sniff(file_field_delimiter_0x3B.csv, 1024)                                                            | 195 us  | 198 us: 1.02x slower    |
| csv_sniff(file_field_delimiter_0x3B.csv, 2048)                                                            | 291 us  | 273 us: 1.07x faster    |
| csv_sniff(file_field_delimiter_0x3B.csv, 4096)                                                            | 300 us  | 275 us: 1.09x faster    |
| csv_sniff(ResultsOR30x500-0.75_3.dat.csv, 1024)                                                           | 71.6 us | 26.1 us: 2.74x faster   |
| csv_sniff(ResultsOR30x500-0.75_3.dat.csv, 2048)                                                           | 106 us  | 54.1 us: 1.95x faster   |
| csv_sniff(ResultsOR30x500-0.75_3.dat.csv, 4096)                                                           | 200 us  | 139 us: 1.44x faster    |
| csv_sniff(prison-and-probation-ombudsman__30-09-2014__justice_PPO-September-Return-senior.csv, 1024)      | 140 us  | 144 us: 1.02x slower    |
| csv_sniff(prison-and-probation-ombudsman__30-09-2014__justice_PPO-September-Return-senior.csv, 2048)      | 182 us  | 181 us: 1.01x faster    |
| csv_sniff(prison-and-probation-ombudsman__30-09-2014__justice_PPO-September-Return-senior.csv, 4096)      | 182 us  | 180 us: 1.01x faster    |
| csv_sniff(fire_archive_V1_50574.csv, 1024)                                                                | 205 us  | 121 us: 1.69x faster    |
| csv_sniff(fire_archive_V1_50574.csv, 2048)                                                                | 206 us  | 122 us: 1.68x faster    |
| csv_sniff(fire_archive_V1_50574.csv, 4096)                                                                | 209 us  | 125 us: 1.67x faster    |
| csv_sniff(file_header_multirow_3.csv, 1024)                                                               | 201 us  | 192 us: 1.05x faster    |
| csv_sniff(file_header_multirow_3.csv, 2048)                                                               | 297 us  | 269 us: 1.11x faster    |
| csv_sniff(file_header_multirow_3.csv, 4096)                                                               | 594 us  | 529 us: 1.12x faster    |
| csv_sniff(row_more_sep_row5_col6.csv, 1024)                                                               | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(row_more_sep_row5_col6.csv, 2048)                                                               | 290 us  | 270 us: 1.08x faster    |
| csv_sniff(row_more_sep_row5_col6.csv, 4096)                                                               | 576 us  | 527 us: 1.09x faster    |
| csv_sniff(1% SiO2_003.csv, 1024)                                                                          | 576 us  | 251 us: 2.30x faster    |
| csv_sniff(1% SiO2_003.csv, 2048)                                                                          | 579 us  | 254 us: 2.28x faster    |
| csv_sniff(1% SiO2_003.csv, 4096)                                                                          | 585 us  | 257 us: 2.28x faster    |
| csv_sniff(extended.csv, 1024)                                                                             | 88.6 us | 33.6 us: 2.64x faster   |
| csv_sniff(extended.csv, 2048)                                                                             | 133 us  | 55.0 us: 2.41x faster   |
| csv_sniff(extended.csv, 4096)                                                                             | 221 us  | 96.7 us: 2.28x faster   |
| csv_sniff(file_header_only.csv, 1024)                                                                     | 45.8 us | 33.3 us: 1.38x faster   |
| csv_sniff(file_header_only.csv, 2048)                                                                     | 46.0 us | 33.2 us: 1.39x faster   |
| csv_sniff(file_header_only.csv, 4096)                                                                     | 45.9 us | 33.3 us: 1.38x faster   |
| csv_sniff(Mixed comma and semicolon-B.csv, 1024)                                                          | 108 us  | 39.6 us: 2.72x faster   |
| csv_sniff(Mixed comma and semicolon-B.csv, 2048)                                                          | 108 us  | 39.7 us: 2.72x faster   |
| csv_sniff(Mixed comma and semicolon-B.csv, 4096)                                                          | 108 us  | 39.7 us: 2.71x faster   |
| csv_sniff(Table embedded in the second record.csv, 1024)                                                  | 191 us  | 85.0 us: 2.25x faster   |
| csv_sniff(Table embedded in the second record.csv, 2048)                                                  | 191 us  | 85.2 us: 2.24x faster   |
| csv_sniff(Table embedded in the second record.csv, 4096)                                                  | 191 us  | 85.0 us: 2.25x faster   |
| csv_sniff(trinity-house__31-03-2015__dft_310315-Trinity-House-Organogram-ver-1-junior.csv, 1024)          | 208 us  | 175 us: 1.19x faster    |
| csv_sniff(trinity-house__31-03-2015__dft_310315-Trinity-House-Organogram-ver-1-junior.csv, 2048)          | 360 us  | 282 us: 1.28x faster    |
| csv_sniff(trinity-house__31-03-2015__dft_310315-Trinity-House-Organogram-ver-1-junior.csv, 4096)          | 666 us  | 478 us: 1.39x faster    |
| csv_sniff(Short pipe separated table embedded.csv, 1024)                                                  | 65.1 us | 33.0 us: 1.97x faster   |
| csv_sniff(Short pipe separated table embedded.csv, 2048)                                                  | 64.5 us | 33.1 us: 1.95x faster   |
| csv_sniff(Short pipe separated table embedded.csv, 4096)                                                  | 64.5 us | 33.0 us: 1.95x faster   |
| csv_sniff(Auto_Tone_sub315_day1.csv, 1024)                                                                | 459 us  | 195 us: 2.36x faster    |
| csv_sniff(Auto_Tone_sub315_day1.csv, 2048)                                                                | 845 us  | 343 us: 2.46x faster    |
| csv_sniff(Auto_Tone_sub315_day1.csv, 4096)                                                                | 1.68 ms | 680 us: 2.47x faster    |
| csv_sniff(row_less_sep_row0_col1.csv, 1024)                                                               | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(row_less_sep_row0_col1.csv, 2048)                                                               | 290 us  | 271 us: 1.07x faster    |
| csv_sniff(row_less_sep_row0_col1.csv, 4096)                                                               | 576 us  | 529 us: 1.09x faster    |
| csv_sniff(W44out.csv, 1024)                                                                               | 74.2 us | 40.2 us: 1.84x faster   |
| csv_sniff(W44out.csv, 2048)                                                                               | 133 us  | 81.4 us: 1.64x faster   |
| csv_sniff(W44out.csv, 4096)                                                                               | 234 us  | 128 us: 1.83x faster    |
| csv_sniff(scottish_law_commission-2011-03-31-organogram-junior.csv, 1024)                                 | 50.9 us | 46.0 us: 1.11x faster   |
| csv_sniff(scottish_law_commission-2011-03-31-organogram-junior.csv, 2048)                                 | 51.1 us | 46.0 us: 1.11x faster   |
| csv_sniff(scottish_law_commission-2011-03-31-organogram-junior.csv, 4096)                                 | 50.9 us | 45.9 us: 1.11x faster   |
| csv_sniff(ResultsOR30x100-0.75_10.dat__m13.csv, 1024)                                                     | 110 us  | 85.5 us: 1.28x faster   |
| csv_sniff(ResultsOR30x100-0.75_10.dat__m13.csv, 2048)                                                     | 187 us  | 146 us: 1.28x faster    |
| csv_sniff(ResultsOR30x100-0.75_10.dat__m13.csv, 4096)                                                     | 282 us  | 211 us: 1.34x faster    |
| csv_sniff(Batch_3250493_batch_results.csv, 1024)                                                          | 127 us  | 141 us: 1.11x slower    |
| csv_sniff(Batch_3250493_batch_results.csv, 2048)                                                          | 220 us  | 229 us: 1.04x slower    |
| csv_sniff(Batch_3250493_batch_results.csv, 4096)                                                          | 343 us  | 321 us: 1.07x faster    |
| csv_sniff(tetranatrolite.csv, 1024)                                                                       | 178 us  | 62.5 us: 2.85x faster   |
| csv_sniff(tetranatrolite.csv, 2048)                                                                       | 178 us  | 62.8 us: 2.84x faster   |
| csv_sniff(tetranatrolite.csv, 4096)                                                                       | 178 us  | 62.7 us: 2.84x faster   |
| csv_sniff(pssave_traindata_m=10_n=10_timelow=15_timehight=30_numofloop=2000.csv, 1024)                    | 170 us  | 47.8 us: 3.56x faster   |
| csv_sniff(pssave_traindata_m=10_n=10_timelow=15_timehight=30_numofloop=2000.csv, 2048)                    | 170 us  | 47.8 us: 3.56x faster   |
| csv_sniff(pssave_traindata_m=10_n=10_timelow=15_timehight=30_numofloop=2000.csv, 4096)                    | 170 us  | 47.8 us: 3.56x faster   |
| csv_sniff(mordenite-dh-2.csv, 1024)                                                                       | 178 us  | 63.5 us: 2.81x faster   |
| csv_sniff(mordenite-dh-2.csv, 2048)                                                                       | 179 us  | 63.9 us: 2.80x faster   |
| csv_sniff(mordenite-dh-2.csv, 4096)                                                                       | 179 us  | 63.8 us: 2.80x faster   |
| csv_sniff(vissim_data_conf2473_i7_v1987.csv, 1024)                                                        | 200 us  | 99.7 us: 2.01x faster   |
| csv_sniff(vissim_data_conf2473_i7_v1987.csv, 2048)                                                        | 202 us  | 101 us: 2.00x faster    |
| csv_sniff(vissim_data_conf2473_i7_v1987.csv, 4096)                                                        | 204 us  | 103 us: 1.98x faster    |
| csv_sniff(Sun2014-Rs.csv, 1024)                                                                           | 192 us  | 81.9 us: 2.34x faster   |
| csv_sniff(Sun2014-Rs.csv, 2048)                                                                           | 192 us  | 81.9 us: 2.34x faster   |
| csv_sniff(Sun2014-Rs.csv, 4096)                                                                           | 191 us  | 81.4 us: 2.35x faster   |
| csv_sniff(download (6).csv, 1024)                                                                         | 448 us  | 311 us: 1.44x faster    |
| csv_sniff(download (6).csv, 2048)                                                                         | 857 us  | 610 us: 1.40x faster    |
| csv_sniff(download (6).csv, 4096)                                                                         | 1.19 ms | 820 us: 1.45x faster    |
| csv_sniff(NBA_scores_out.csv, 1024)                                                                       | 148 us  | 114 us: 1.29x faster    |
| csv_sniff(NBA_scores_out.csv, 2048)                                                                       | 235 us  | 160 us: 1.47x faster    |
| csv_sniff(NBA_scores_out.csv, 4096)                                                                       | 272 us  | 176 us: 1.54x faster    |
| csv_sniff(Auto_Tone_sub205_over.csv, 1024)                                                                | 449 us  | 194 us: 2.32x faster    |
| csv_sniff(Auto_Tone_sub205_over.csv, 2048)                                                                | 841 us  | 348 us: 2.42x faster    |
| csv_sniff(Auto_Tone_sub205_over.csv, 4096)                                                                | 1.65 ms | 682 us: 2.42x faster    |
| csv_sniff(workforce-management-information-dft_201706.csv, 1024)                                          | 227 us  | 165 us: 1.37x faster    |
| csv_sniff(workforce-management-information-dft_201706.csv, 2048)                                          | 637 us  | 440 us: 1.45x faster    |
| csv_sniff(workforce-management-information-dft_201706.csv, 4096)                                          | 895 us  | 662 us: 1.35x faster    |
| csv_sniff(rape_table_3_prosecution_outcomes_0708_1314.csv, 1024)                                          | 229 us  | 166 us: 1.38x faster    |
| csv_sniff(rape_table_3_prosecution_outcomes_0708_1314.csv, 2048)                                          | 376 us  | 278 us: 1.35x faster    |
| csv_sniff(rape_table_3_prosecution_outcomes_0708_1314.csv, 4096)                                          | 375 us  | 278 us: 1.35x faster    |
| csv_sniff(Auto_Tone_sub242_nov.csv, 1024)                                                                 | 592 us  | 226 us: 2.62x faster    |
| csv_sniff(Auto_Tone_sub242_nov.csv, 2048)                                                                 | 1.13 ms | 412 us: 2.74x faster    |
| csv_sniff(Auto_Tone_sub242_nov.csv, 4096)                                                                 | 2.18 ms | 789 us: 2.76x faster    |
| csv_sniff(S39.csv, 1024)                                                                                  | 186 us  | 78.5 us: 2.36x faster   |
| csv_sniff(S39.csv, 2048)                                                                                  | 188 us  | 80.6 us: 2.33x faster   |
| csv_sniff(S39.csv, 4096)                                                                                  | 191 us  | 84.5 us: 2.27x faster   |
| csv_sniff(Wine_Cellar_Consumption_dataset_14-15.csv, 1024)                                                | 447 us  | 330 us: 1.36x faster    |
| csv_sniff(Wine_Cellar_Consumption_dataset_14-15.csv, 2048)                                                | 912 us  | 649 us: 1.41x faster    |
| csv_sniff(Wine_Cellar_Consumption_dataset_14-15.csv, 4096)                                                | 1.67 ms | 1.15 ms: 1.46x faster   |
| csv_sniff(file_record_delimiter_0xA.csv, 1024)                                                            | 194 us  | 196 us: 1.01x slower    |
| csv_sniff(file_record_delimiter_0xA.csv, 2048)                                                            | 290 us  | 270 us: 1.08x faster    |
| csv_sniff(file_record_delimiter_0xA.csv, 4096)                                                            | 576 us  | 527 us: 1.09x faster    |
| csv_sniff(movies-condensed.csv, 1024)                                                                     | 158 us  | 161 us: 1.02x slower    |
| csv_sniff(movies-condensed.csv, 2048)                                                                     | 263 us  | 255 us: 1.03x faster    |
| csv_sniff(movies-condensed.csv, 4096)                                                                     | 344 us  | 320 us: 1.08x faster    |
| csv_sniff(Sustainability_-_Water_consumption_P_56.csv, 1024)                                              | 102 us  | 78.1 us: 1.31x faster   |
| csv_sniff(Sustainability_-_Water_consumption_P_56.csv, 2048)                                              | 102 us  | 78.3 us: 1.31x faster   |
| csv_sniff(Sustainability_-_Water_consumption_P_56.csv, 4096)                                              | 102 us  | 78.1 us: 1.31x faster   |
| csv_sniff(Consular_cases_April_2016.csv, 1024)                                                            | 78.3 us | 73.6 us: 1.06x faster   |
| csv_sniff(Consular_cases_April_2016.csv, 2048)                                                            | 112 us  | 99.0 us: 1.13x faster   |
| csv_sniff(Consular_cases_April_2016.csv, 4096)                                                            | 316 us  | 211 us: 1.50x faster    |
| csv_sniff(Camp Palacios - Wind Direction.csv, 1024)                                                       | 727 us  | 180 us: 4.04x faster    |
| csv_sniff(Camp Palacios - Wind Direction.csv, 2048)                                                       | 1.40 ms | 348 us: 4.03x faster    |
| csv_sniff(Camp Palacios - Wind Direction.csv, 4096)                                                       | 2.79 ms | 704 us: 3.96x faster    |
| csv_sniff(hist_2000_15O.csv, 1024)                                                                        | 101 us  | 33.3 us: 3.03x faster   |
| csv_sniff(hist_2000_15O.csv, 2048)                                                                        | 174 us  | 67.1 us: 2.60x faster   |
| csv_sniff(hist_2000_15O.csv, 4096)                                                                        | 317 us  | 116 us: 2.74x faster    |
| csv_sniff(ResultsOR30x250-0.50_4.dat.csv, 1024)                                                           | 72.4 us | 30.5 us: 2.37x faster   |
| csv_sniff(ResultsOR30x250-0.50_4.dat.csv, 2048)                                                           | 135 us  | 92.5 us: 1.46x faster   |
| csv_sniff(ResultsOR30x250-0.50_4.dat.csv, 4096)                                                           | 224 us  | 170 us: 1.32x faster    |
| csv_sniff(file_multitable_more.csv, 1024)                                                                 | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(file_multitable_more.csv, 2048)                                                                 | 290 us  | 269 us: 1.08x faster    |
| csv_sniff(file_multitable_more.csv, 4096)                                                                 | 575 us  | 529 us: 1.09x faster    |
| csv_sniff(row_extra_quote5_col3.csv, 1024)                                                                | 195 us  | 196 us: 1.01x slower    |
| csv_sniff(row_extra_quote5_col3.csv, 2048)                                                                | 290 us  | 270 us: 1.07x faster    |
| csv_sniff(row_extra_quote5_col3.csv, 4096)                                                                | 576 us  | 527 us: 1.09x faster    |
| csv_sniff(Camp Palacios - Humidity.csv, 1024)                                                             | 769 us  | 202 us: 3.80x faster    |
| csv_sniff(Camp Palacios - Humidity.csv, 2048)                                                             | 1.57 ms | 410 us: 3.84x faster    |
| csv_sniff(Camp Palacios - Humidity.csv, 4096)                                                             | 3.15 ms | 827 us: 3.81x faster    |
| csv_sniff(Undefined field delimiter.csv, 1024)                                                            | 133 us  | 92.4 us: 1.44x faster   |
| csv_sniff(Undefined field delimiter.csv, 2048)                                                            | 133 us  | 92.4 us: 1.44x faster   |
| csv_sniff(Undefined field delimiter.csv, 4096)                                                            | 133 us  | 92.3 us: 1.44x faster   |
| Geometric mean                                                                                            | (ref)   | 1.50x faster            |

Benchmark hidden because not significant (2): csv_sniff(file_no_header.csv, 1024), csv_sniff(senior-staff-march-2020.csv, 1024)

# Commands

```
(main) % ./python bench.py --rigorous -o 508a00ceb2eb2d7835c1f72fabf8873232384d09.main.json
```

```
(csv-sniffer-counter-set) ./python bench.py --rigorous -o 2f1ea73be0589e4baa4ca8d219c6963871a24855.csv-sniffer-counter-set.json
```

# Environment

```
% ./python -c "import sysconfig; print(sysconfig.get_config_var('CONFIG_ARGS'))"
'--with-lto' '--enable-optimizations'
```

`sudo ./python -m pyperf system tune` ensured.
