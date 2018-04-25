//Circular String Rotation Matching
//given two strings s and t eval if they 're a circular rotation mathing of each other
package main
import (
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
	var a string = "abracadabra"
	var b string = "dabraabraca"
	//fmt.Print(hello)
	aux := []byte(a)
	i := 0
	for i<len(aux){
		i++
		if (isEqual(string(aux),b)){
			fmt.Println("%s es una rotacion de %s",a,b)
			i=len(aux)
		}
		fmt.Println(string(aux))
		aux=rotate(aux)
	}
}