pragma solidity 0.8.6;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Pixellions is ERC721URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;


    uint128 public constant pixels = 1000000;
    uint256 public constant start_price = 0.001 ether;

    mapping(address => uint256) owner_pixels;

    constructor() ERC721("Pixellions", "PXL") {

    }

    // function mintPixel(string memory) public returns ()
}