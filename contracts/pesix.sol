pragma solidity ^0.4.20;

contract pesix {

  mapping (address => string) address_to_name;
  mapping (address => uint) user_to_score;
  mapping (address => uint[]) user_to_history;

  address[] public no_of_users;
  address[] public filtered_no_of_users;

  function add_user(string name) public {
    address_to_name[msg.sender] = name;
    user_to_score[msg.sender] = 0;
    // user_to_history[msg.sender] = [];
    no_of_users.push(msg.sender);
  }

  function add_order(uint carbon_emm) public {
    user_to_history[msg.sender].push(carbon_emm);
  }

  function update_score(address user,uint new_score) public {
    user_to_score[user] = new_score;
  }

  function view_score() view  public returns(uint) {
    return user_to_score[msg.sender];
  }

  function view_score_by_address(address user) view public returns(uint) {
      return user_to_score[user];
  }

  function view_history() view public returns(uint[]) {
    return user_to_history[msg.sender];
  }

  function view_history_by_address(address user) view public returns(uint[]) {
      return user_to_history[user];
  }

  function show_filtered_users() view public returns(address[]) {
      return filtered_no_of_users;
  }

//   function generate_leaderboard() public {
//     sort_array(no_of_users);
//   }

  function sort_array() public {
      for(uint k=0; k<no_of_users.length;k++)
      {
          if(user_to_score[no_of_users[k]]!=0)
          {
              filtered_no_of_users.push(no_of_users[k]);
          }
      }
        uint256 l = filtered_no_of_users.length;
        for(uint i = 0; i < l; i++) {
            for(uint j = i+1; j < l ;j++) {
                if(user_to_score[filtered_no_of_users[i]] < user_to_score[filtered_no_of_users[j]]) {
                    address temp = filtered_no_of_users[i];
                    filtered_no_of_users[i] = filtered_no_of_users[j];
                    filtered_no_of_users[j] = temp;
                }
            }
        }

}

}
