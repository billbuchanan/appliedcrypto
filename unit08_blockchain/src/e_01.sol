pragma solidity ^0.4.0;

contract mymath {
   function sqrt(uint x) constant returns (uint y) {
    uint z = (x + 1) / 2;
    y = x;
    while (z < y) {
        y = z;
        z = (x / z + z) / 2;
    }
}
}
