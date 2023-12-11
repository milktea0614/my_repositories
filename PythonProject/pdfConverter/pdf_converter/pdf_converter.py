import os
import pathlib
import fitz
import cv2

from miraelogger import Logger

MODUL_LOGGER = Logger(log_name=__name__).logger


def convert_to_bw_and_increase_contrast(input_pdf_path, output_pdf_path, contrast=1.5, brightness=1.5):
    # PDF 파일 열기
    input_pdf = fitz.open(input_pdf_path)
    result_pdf = fitz.open()

    # 모든 페이지에 대해 작업 수행
    MODUL_LOGGER.info(f"Total page: {input_pdf.page_count}")
    MODUL_LOGGER.info(f"Contrast: {contrast}, Brightness: {brightness}")
    MODUL_LOGGER.info(f"Convert Start...")
    for page_num in range(input_pdf.page_count):
        MODUL_LOGGER.debug(f"Current page: {page_num+1}")

        page = input_pdf[page_num]
        _file_name = pathlib.Path(__file__).resolve().parent / f"_img/{page_num}_gray.png"
        current = page.get_pixmap(matrix=fitz.Matrix(3, 3), colorspace=fitz.csGRAY)
        current.save(_file_name, 'png')

        _convert_name = pathlib.Path(__file__).resolve().parent / f"_img/{page_num}_convert.png"
        _previous = cv2.imread(str(_file_name))
        _contrast = cv2.convertScaleAbs(_previous, alpha=contrast, beta=brightness)
        cv2.imwrite(str(_convert_name), _contrast)
        os.remove(str(_file_name))

        tmp = fitz.open(_convert_name)
        _temp_rect = tmp[0].rect  # image dimension
        _temp_bytes = tmp.convert_to_pdf()
        tmp.close()
        os.remove(str(_convert_name))

        _tmp_pdf = fitz.open("pdf", _temp_bytes)

        result_pdf.insert_pdf(_tmp_pdf, from_page=0, to_page=0)
        _tmp_pdf.close()

    # 변환된 PDF 저장
    result_pdf.save(output_pdf_path)
    result_pdf.close()
    input_pdf.close()


# 사용 예제
my_contrast = 1.1
my_brightness = 0.25

input_pdf_path = "D:\\03_Study\\Certification\\2 SQLD (국가공인 SQL 개발자)(영구습득)\\이기적 SQLD - 문제 모음.pdf"  # 원본 PDF 파일 경로
output_pdf_path = str(pathlib.Path(__file__).resolve().parent / f"output_bw_and_contrast({str(my_contrast).replace('.', '_')}&{str(my_brightness).replace('.', '_')}).pdf")  # 결과 파일 경로

MODUL_LOGGER.info(f"Target PDF: {input_pdf_path}")

convert_to_bw_and_increase_contrast(input_pdf_path, output_pdf_path, my_contrast, my_brightness)

MODUL_LOGGER.info(f"Result PDF: {output_pdf_path}")