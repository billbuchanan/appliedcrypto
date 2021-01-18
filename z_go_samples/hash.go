package main

import (
"crypto/rand"
"golang.org/x/crypto/md4"
"crypto/md5"
"crypto/sha1"
"crypto/sha256"
"crypto/sha512"
"golang.org/x/crypto/ripemd160"
"golang.org/x/crypto/sha3"
"golang.org/x/crypto/blake2b"
"golang.org/x/crypto/scrypt"
"golang.org/x/crypto/argon2"
"golang.org/x/crypto/bcrypt"
"fmt"
"flag"
)

type params struct {
    memory      uint32
    iterations  uint32
    parallelism uint8
    saltLength  uint32
    keyLength   uint32
}

func generateRandomBytes(n uint32) ([]byte, error) {
    b := make([]byte, n)
    _, err := rand.Read(b)
    if err != nil {
        return nil, err
    }

    return b, nil
}

func main() {
    s := "abc"
    flag.Parse()
    args := flag.Args()
    s=args[0]



    h1 := md4.New()
    h2 := md5.Sum([]byte(s))
    h3 := sha1.Sum([]byte(s))
    h4 := sha256.Sum256([]byte(s))
    h5 := sha512.Sum512([]byte(s))
    h6 := ripemd160.New()
    h7 := sha3.Sum256([]byte(s))
    h8 := sha3.Sum512([]byte(s))
    h9 := blake2b.Sum256([]byte(s))
    h10 := blake2b.Sum512([]byte(s))


    p := &params{
        memory:      64 * 1024,
        iterations:  1,
        parallelism: 1,
        saltLength:  16,
        keyLength:   32,
    }

    salt, err := generateRandomBytes(p.saltLength)
    h11 := argon2.IDKey([]byte(s), salt, p.iterations, p.memory, p.parallelism, p.keyLength)



    // Values are password, salt, N, r, p, key length
    h12, err := scrypt.Key([]byte(s), salt, 1<<15, 4, 1, 32)

    cost:=1

    h13,err:=bcrypt.GenerateFromPassword([]byte(s), cost) 

    h1.Write([]byte(s))
    h6.Write([]byte(s))



    fmt.Println("Input: ",s)
    fmt.Printf("MD4: %x\n", h1.Sum(nil))
    fmt.Printf("MD5: %x\n", h2)
    fmt.Printf("SHA-1: %x\n", h3)
    fmt.Printf("SHA-256: %x\n", h4)
    fmt.Printf("SHA-512: %x\n", h5)
    fmt.Printf("RIPEMD160: %x\n", h6.Sum(nil))
    fmt.Printf("SHA-3 256: %x\n", h7)
    fmt.Printf("SHA-3 512: %x\n", h8)
    fmt.Printf("Blake2b 256-bit: %x\n", h9)   
    fmt.Printf("Blake2b 512-bit: %x\n", h10)    
    if (err==nil) {
     fmt.Printf("Argon2: %x\n", h11) 
     fmt.Printf("Scrypt: %x\n", h12) 
     fmt.Printf("BCrypt: %s\n", h13) 
    } 
 
        

}
