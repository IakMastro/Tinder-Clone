package com.example.tinder_clone_android;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import com.example.TinderCloneAdapter;
import com.example.tinder_clone_android.json_api.RestApi;
import com.example.tinder_clone_android.json_api.User;
import com.example.tinder_clone_android.json_api.UserList;
import com.squareup.picasso.Picasso;

import java.time.LocalDate;
import java.time.Period;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {
    public static MainActivity Instance;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Instance = this;

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.1.3:5000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        RestApi restApi = retrofit.create(RestApi.class);

        Call<UserList> call = restApi.getUsers();

        call.enqueue(new Callback<UserList>() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onResponse(Call<UserList> call, Response<UserList> response) {
                if (!response.isSuccessful()) {
                    System.err.printf("*** Code: %s\n", response.code());
                    return;
                }

                UserList userList = response.body();
                assert userList != null;

                RecyclerView recyclerView = findViewById(R.id.recycler_view);
                TinderCloneAdapter tinderCloneAdapter =
                        new TinderCloneAdapter(userList.getUserList());
                recyclerView.setAdapter(tinderCloneAdapter);
                recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.Instance));
            }

            @Override
            public void onFailure(Call<UserList> call, Throwable t) {
                System.err.printf("*** %s\n", t.getMessage());
            }
        });
    }
}