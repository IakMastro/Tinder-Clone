package com.example.tinder_clone_android.json_api;

import retrofit2.Call;
import retrofit2.http.GET;

public interface RestApi {
    @GET("ping")
    Call<Ping> getPing();

    @GET("/")
    Call<UserList> getUsers();
}
