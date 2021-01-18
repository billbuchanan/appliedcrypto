package main

import (
"golang.org/x/crypto/nacl/box"
"crypto/rand"
"io"
 "fmt"
"flag"
)



func main() {

 flag.Parse()
 args := flag.Args()

 message:=args[0]

AlicePublicKey, AlicePrivateKey, _ := box.GenerateKey(rand.Reader)

fmt.Printf("Alice private %x\n",*AlicePrivateKey)
fmt.Printf("Alice public (x-co-ord) %x\n",*AlicePublicKey)

BobPublicKey, BobPrivateKey, _ := box.GenerateKey(rand.Reader)


fmt.Printf("\nBob private %x\n",*BobPrivateKey)
fmt.Printf("Bob public (x-co-ord) %x\n",*BobPublicKey)


var nonce [24]byte

io.ReadFull(rand.Reader, nonce[:])

msg := []byte(message)

encrypted := box.Seal(nonce[:], msg, &nonce, BobPublicKey, AlicePrivateKey)

var decryptNonce [24]byte

copy(decryptNonce[:], encrypted[:24])

decrypted, _ := box.Open(nil, encrypted[24:], &decryptNonce, AlicePublicKey, BobPrivateKey)

fmt.Printf("\nMessage: %s\n",message)
fmt.Printf("\nEncrypted: %x\n\n",encrypted)
fmt.Printf("Decrypted %s",string(decrypted))

}

