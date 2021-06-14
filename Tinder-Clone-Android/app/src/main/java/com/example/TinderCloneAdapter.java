package com.example;

import android.annotation.SuppressLint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.tinder_clone_android.R;
import com.example.tinder_clone_android.json_api.User;
import com.squareup.picasso.Picasso;

import org.jetbrains.annotations.NotNull;

import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class TinderCloneAdapter extends RecyclerView.Adapter<TinderCloneAdapter.ViewHolder> {
    private final ArrayList<User> localDataSet;

    public TinderCloneAdapter(ArrayList<User> localDataSet) {
        this.localDataSet = localDataSet;
    }

    @NonNull
    @NotNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull @NotNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.list_item, parent, false);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull @NotNull ViewHolder holder, int position) {
        holder.bind(localDataSet.get(position));
    }

    @Override
    public int getItemCount() {
        return localDataSet.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        private ImageView imageView;
        private TextView name;
        private TextView surname;
        private TextView age;
        private TextView height;
        private TextView weight;
        private TextView eyes;
        private TextView hair;

        @SuppressLint("SetTextI18n")
        public void bind(User user) {

            Picasso.get()
                    .load("http://192.168.1.3:5000/img/".concat(user.getPfp()))
                    .error(R.drawable.ic_launcher_background).into(imageView);

            name.setText(user.getName());
            surname.setText(user.getSurname());
            age.setText(Period.between(LocalDate
                    .parse(user.getBirthday()), LocalDate.now()).getYears() + " years old");
            height.setText(user.getHeight() + "cm");
            weight.setText(user.getWeight() + "kg");
            eyes.setText(user.getEyeColour() + " eyes, ");
            hair.setText(user.getHairColour() + " hair");
        }

        public ViewHolder(@NonNull @NotNull View itemView) {
            super(itemView);
            setReferences(itemView);
        }

        private void setReferences(View itemView) {
            imageView = itemView.findViewById(R.id.profile_pic);
            name = itemView.findViewById(R.id.name);
            surname = itemView.findViewById(R.id.surname);
            age = itemView.findViewById(R.id.age);
            height = itemView.findViewById(R.id.height);
            weight = itemView.findViewById(R.id.weight);
            eyes = itemView.findViewById(R.id.eyes);
            hair = itemView.findViewById(R.id.hair);
        }
    }
}