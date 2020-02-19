import os
from OpenSSL import crypto

DEFAULT_CA_KEY = 'CA_KEY.key'
DEFAULT_CA_CRT = 'CA_CRT.crt'


# Класс, генерирующий сертификаты
class CertificateGenerator:
    def __init__(self, params):
        self.cert_dir = params['Cert dir']
        self.key_file = params['Key file name']
        self.cert_file = params['Cert file name']
        # Ключ, которым производится подпись
        if 'CA key path' in params.keys():
            self.ca_key = params['CA key path']
        else:
            self.ca_key = DEFAULT_CA_KEY
        # Сертификат, которым производится подпись
        if 'CA cert path' in params.keys():
            self.ca_crt = params['CA cert path']
        else:
            self.ca_crt = DEFAULT_CA_CRT
        self.params = params
        # Значения статуса генерации сертификата
        self.success = True

    def create_self_signed_cert(self):
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # Создание сертификата
        cert = crypto.X509()

        # Установка значений опций, указанных пользователем на экране с заданием параметров сертификата
        subj = cert.get_subject()
        for (key, value) in self.params.items():
            if key in {'C', 'ST', 'L', 'O', 'OU', 'CN'}:
                setattr(subj, key, value)

        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        # Срок жизни сертификата
        cert.gmtime_adj_notAfter(1*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, "sha1")

        self.__output_certs(cert, k)

        return self.success

    def create_signed_cert(self):
        # Сертификат, который заверит создаваемый сертификат
        ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(self.ca_crt, 'rb').read())
        # Ключ сертификата, который заверит создаваемый сертификат
        ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, open(self.ca_key).read())

        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # Создание сертификата
        cert = crypto.X509()

        # Установка значений опций, указанных пользователем на экране с заданием параметров сертификата
        subj = cert.get_subject()
        for (key, value) in self.params.items():
            if key in {'C', 'ST', 'L', 'O', 'OU', 'CN'}:
                setattr(subj, key, value)

        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        # Срок жизни сертификата
        cert.gmtime_adj_notAfter(1*365*24*60*60)
        cert.set_issuer(ca_cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(ca_key, "sha1")

        self.__output_certs(cert, k)

        return self.success

    # Сохранение сертификата и приватного ключа в файлы
    def __output_certs(self, cert, k):
        with open(os.path.join(self.cert_dir, self.cert_file), "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

        with open(os.path.join(self.cert_dir, self.key_file), "wb") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
