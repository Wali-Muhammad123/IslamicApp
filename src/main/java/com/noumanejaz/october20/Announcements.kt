package com.noumanejaz.october20

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem

class Announcements : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_announcements)
        supportActionBar?.setTitle("Namaz")
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.announcements_menu,menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when(item.itemId){
            R.id.backToMainActivity->{
                val intent= Intent(this,MainActivity::class.java)
                startActivity(intent)
                return true
            }
            else-> super.onOptionsItemSelected(item)
        }

    }
}