//Circular String Rotation Matching
//given two strings s and t eval if they 're a circular rotation mathing of each other
package main
import (
		"os"
		"fmt"
)
func rotate(slice []byte) []byte {
	//slice:=[]byte(a)
	end :=slice[0]
	for i := 0; i < len(slice)-1; i++ {
		slice[i]=slice[i+1]
	}
	slice[len(slice)-1]=end
	return slice
}
func isEqual(a,b string) bool{
	if a == b {
		return true
	}
	return false
}

func main() {
	//var hello string ="hola\n"
	//var a string = "abracadabra"
	var s1 string = os.Args[1]
	//var b string = "dabraabraca"
	var s2 string = os.Args[2]
	var match bool = false
	//fmt.Print(hello)
	aux := []byte(s2)
	i := 0
	for i<len(aux){
		i++
		if (isEqual(string(aux),s1)){
			fmt.Printf("%s es una rotacion de %s\n",s2,s1)
			match = true
			i=len(aux)
		}
		//fmt.Println(string(aux))
		aux=rotate(aux)
	}
	if !match {
		fmt.Printf("%s no es una rotacion de %s\n",s2,s1)
	}
}