import os
from tqdm import tqdm

# 시저 암호화 함수
def encrypt(text, shift):
    result = ""
    shift = shift % 26  # shift 값을 0~25로 조정
    for char in tqdm(text, desc="암호화 진행 중", leave=False):
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # 비영어 문자는 그대로
    return result

# 시저 복호화 함수
def decrypt(text, shift):
    result = ""
    shift = shift % 26
    for char in tqdm(text, desc="복호화 진행 중", leave=False):
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# 파일 암호화 함수 (파일 전체 처리)
def encrypt_file(input_file, shift):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()  # 파일 전체 읽기
            encrypted_text = encrypt(text, shift)  # 전체 텍스트 암호화

        file_dir = os.path.dirname(input_file)
        output_file = os.path.join(file_dir, f"encrypted_{os.path.basename(input_file)}")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

        print(f"암호화된 텍스트 미리보기 (처음 100글자): {encrypted_text[:100]}")
        print(f"'{input_file}' 파일이 암호화되어 '{output_file}'에 저장되었습니다.")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {input_file}")
    except PermissionError:
        print(f"파일에 접근할 수 없습니다: {input_file}")
    except UnicodeDecodeError:
        print(f"파일을 읽는 중 인코딩 오류가 발생했습니다. '{input_file}' 파일의 인코딩을 확인해주세요.")
    except Exception as e:
        print(f"파일 암호화 중 오류 발생: {e}")

# 파일 복호화 함수 (파일 전체 처리)
def decrypt_file(input_file, shift):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()  # 파일 전체 읽기
            decrypted_text = decrypt(text, shift)  # 전체 텍스트 복호화

        file_dir = os.path.dirname(input_file)
        output_file = os.path.join(file_dir, f"decrypted_{os.path.basename(input_file)}")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_text)

        print(f"복호화된 텍스트 미리보기 (처음 100글자): {decrypted_text[:100]}")
        print(f"'{input_file}' 파일이 복호화되어 '{output_file}'에 저장되었습니다.")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {input_file}")
    except PermissionError:
        print(f"파일에 접근할 수 없습니다: {input_file}")
    except UnicodeDecodeError:
        print(f"파일을 읽는 중 인코딩 오류가 발생했습니다. '{input_file}' 파일의 인코딩을 확인해주세요.")
    except Exception as e:
        print(f"파일 복호화 중 오류 발생: {e}")

# 파일이 존재하는지 확인
def check_file_exists(file_path):
    return os.path.isfile(file_path)

# 메인 함수
def main():
    print("시저 암호화 프로그램입니다.")
    
    while True:
        print("\n1. 텍스트 암호화\n2. 텍스트 복호화\n3. 파일 암호화\n4. 파일 복호화\n9. 종료")
        
        try:
            select = input("작업을 선택하세요 (1/2/3/4/9): ")
            
            if select == '9':
                print("프로그램을 종료합니다.")
                break
            
            elif select == '1':
                text = input("암호화할 텍스트를 입력하세요: ")
                shift = int(input("Shift 값을 입력하세요: "))
                if shift < 0:
                    raise ValueError("Shift 값은 0 이상의 정수여야 합니다.")
                encrypted_text = encrypt(text, shift)
                print(f"암호화된 텍스트: {encrypted_text}")
                
            elif select == '2':
                text = input("복호화할 텍스트를 입력하세요: ")
                shift = int(input("Shift 값을 입력하세요: "))
                if shift < 0:
                    raise ValueError("Shift 값은 0 이상의 정수여야 합니다.")
                decrypted_text = decrypt(text, shift)
                print(f"복호화된 텍스트: {decrypted_text}")
                
            elif select == '3':
                input_file = input("암호화할 파일 경로를 입력하세요: ")
                if check_file_exists(input_file):
                    shift = int(input("Shift 값을 입력하세요: "))
                    if shift < 0:
                        raise ValueError("Shift 값은 0 이상의 정수여야 합니다.")
                    encrypt_file(input_file, shift)
                else:
                    print("파일이 존재하지 않습니다.")
                    
            elif select == '4':
                input_file = input("복호화할 파일 경로를 입력하세요: ")
                if check_file_exists(input_file):
                    shift = int(input("Shift 값을 입력하세요: "))
                    if shift < 0:
                        raise ValueError("Shift 값은 0 이상의 정수여야 합니다.")
                    decrypt_file(input_file, shift)
                else:
                    print("파일이 존재하지 않습니다.")
                    
            else:
                raise ValueError("1, 2, 3, 4 또는 9만 입력 가능합니다.")
        
        except ValueError as ve:
            print(f"입력 오류 발생: {ve}, 다시 시도하세요.")
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}, 다시 시도해주세요.")

if __name__ == "__main__":
    main()