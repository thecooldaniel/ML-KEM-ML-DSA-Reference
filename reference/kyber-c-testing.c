#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include "./kyber-c/ref/params.h"
#include "./kyber-c/ref/fips202.h"
#include "./kyber-c/ref/kem.h"

extern void sha3_256(uint8_t h[32], const uint8_t *in, size_t inlen);
extern void sha3_512(uint8_t h[64], const uint8_t *in, size_t inlen);

extern void print_hex_bytes(unsigned char *in, size_t len);

#define hash_h(OUT, IN, INBYTES) sha3_256(OUT, IN, INBYTES)
#define hash_g(OUT, IN, INBYTES) sha3_512(OUT, IN, INBYTES)

// void print_hex_bytes(unsigned char *in, size_t len) {
//     printf("0x");
//     for(int i = 0; i < len; i++) {
//         printf("%02X", (unsigned char)in[i]);
//     }
//     printf("\n");
// }


int main(void) {

    uint8_t in[4] = {0xef, 0xbe, 0xad, 0xde};
    uint8_t htest[32];
    uint8_t gtest[64];

    // printf("testing printf");

    hash_h(htest, in, 4);
    hash_g(gtest, in, 4);

    print_hex_bytes(htest, 32);
    print_hex_bytes(gtest, 64);

    // uint8_t pk[800];
    // uint8_t sk[768]; // Kyber 512 params

    // from kyber_c/ref/test_keys.c
    uint8_t pk[CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[CRYPTO_SECRETKEYBYTES];
    uint8_t ct[CRYPTO_CIPHERTEXTBYTES];
    uint8_t key_a[CRYPTO_BYTES];
    uint8_t key_b[CRYPTO_BYTES] = {0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde, 0xef, 0xbe, 0xad, 0xde};
    
    //Alice generates a public key
    crypto_kem_keypair(pk, sk);

    // ref/kem.c -> ref/indcpa.c:indcpa_enc()
    //Bob derives a secret key and creates a response
    crypto_kem_enc(ct, key_b, pk);

    //Alice uses Bobs response to get her shared key
    crypto_kem_dec(key_a, ct, sk);

    if(memcmp(key_a, key_b, CRYPTO_BYTES)) {
        printf("ERROR keys\n");
        return 1;
    }
    

    return 0;

}