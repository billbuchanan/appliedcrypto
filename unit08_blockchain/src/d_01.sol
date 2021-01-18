pragma solidity >0.4.0;
contract test2{
   uint a ;
   constructor () public {
       a = 1;
   }
   function val() public returns(uint){
       return a;
   }  
}
contract test3 is test2{ 
    uint b = a++;
    function show() public returns(uint){
        return b; 
    }
}
