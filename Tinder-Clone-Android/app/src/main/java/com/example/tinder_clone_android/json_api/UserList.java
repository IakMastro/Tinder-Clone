package com.example.tinder_clone_android.json_api;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class UserList {
    @SerializedName("users")
    private ArrayList<User> userList;

    public ArrayList<User> getUserList() {
        return userList;
    }

    public void setUserList(ArrayList<User> userList) {
        this.userList = userList;
    }
}
