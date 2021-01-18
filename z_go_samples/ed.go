package main

import (
	"fmt"
        "flag"
	"gopkg.in/dedis/kyber.v2"
	"gopkg.in/dedis/kyber.v2/group/edwards25519"
)

var curve = edwards25519.NewBlakeSHA256Ed25519()
var sha256 = curve.Hash()

type Signature struct {
	r kyber.Point
	s kyber.Scalar
}

func Hash(s string) kyber.Scalar {
	sha256.Reset()
	sha256.Write([]byte(s))

	return curve.Scalar().SetBytes(sha256.Sum(nil))
}

// m: Message
// x: Private key
func Sign(m string, x kyber.Scalar) Signature {
	// Get the base of the curve.
	g := curve.Point().Base()

	// Pick a random k from allowed set.
	k := curve.Scalar().Pick(curve.RandomStream())

	// r = k * G (a.k.a the same operation as r = g^k)
	r := curve.Point().Mul(k, g)

	// Hash(m || r)
	e := Hash(m + r.String())

	// s = k - e * x
	s := curve.Scalar().Sub(k, curve.Scalar().Mul(e, x))

	return Signature{r: r, s: s}
}

// m: Message
// S: Signature
func PublicKey(m string, S Signature) kyber.Point {
	// Create a generator.
	g := curve.Point().Base()

	// e = Hash(m || r)
	e := Hash(m + S.r.String())

	// y = (r - s * G) * (1 / e)
	y := curve.Point().Sub(S.r, curve.Point().Mul(S.s, g))
	y = curve.Point().Mul(curve.Scalar().Div(curve.Scalar().One(), e), y)

	return y
}

// m: Message
// s: Signature
// y: Public key
func Verify(m string, S Signature, y kyber.Point) bool {
	// Create a generator.
	g := curve.Point().Base()

	// e = Hash(m || r)
	e := Hash(m + S.r.String())

	// Attempt to reconstruct 's * G' with a provided signature; s * G = r - e * y
	sGv := curve.Point().Sub(S.r, curve.Point().Mul(e, y))

	// Construct the actual 's * G'
	sG := curve.Point().Mul(S.s, g)

	// Equality check; ensure signature and public key outputs to s * G.
	return sG.Equal(sGv)
}
func (S Signature) String() string {
	return fmt.Sprintf("(r=%s, s=%s)", S.r, S.s)
}


func main() {

    message := "abc"
    flag.Parse()
    args := flag.Args()
    message=args[0]

	privateKey := curve.Scalar().Pick(curve.RandomStream())
	publicKey := curve.Point().Mul(privateKey, curve.Point().Base())

fmt.Printf("Message to sign: %s\n\n", message)
	fmt.Printf("Private key: %s\n", privateKey)
	fmt.Printf("Public key: %s\n\n", publicKey)

	signature := Sign(message, privateKey)

        fmt.Printf("Signature (r=%s, s=%s)\n\n", signature.r, signature.s)

	derivedPublicKey := PublicKey(message, signature)

	fmt.Printf("Derived public key: %s\n\n", derivedPublicKey)

	fmt.Printf("Checking keys %t\n", publicKey.Equal(derivedPublicKey))
	fmt.Printf("Checking signature %t\n\n", Verify(message, signature, publicKey))


}
