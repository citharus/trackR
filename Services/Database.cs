using System;
using Microsoft.EntityFrameworkCore;
using trackR.Models;

namespace trackR.Services;

public class Database : DbContext
{
    public DbSet<DbEntry> Entries { get; set; } = null!;

    private string DbPath { get; }

    public Database()
    {
        const Environment.SpecialFolder folder = Environment.SpecialFolder.LocalApplicationData;
        var path = Environment.GetFolderPath(folder);
        DbPath = System.IO.Path.Join(path, "database.db");
    }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseSqlite($"Data Source={DbPath}");
}