using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace DataVisualization.Database.Models
{
    /// <summary>
    /// Representação do banco de dados para a aplicação
    /// </summary>
    public partial class TweetsContext : DbContext
    {
        public TweetsContext()
        {
        }

        public TweetsContext(DbContextOptions<TweetsContext> options)
            : base(options)
        {
        }
        #region Public properties
        /// <summary>
        /// Os estados para a aplicação
        /// </summary>
        public virtual DbSet<Estados> Estados { get; set; }
        #endregion
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer("Data Source=127.0.0.1,1433; Initial Catalog=Tweets;User Id=sa; Password=Banana123");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Estados>(entity =>
            {
                if(Database.ProviderName == "Microsoft.EntityFrameworkCore.InMemory")
                {
                    entity.HasNoKey();

                    entity.Property(e => e.Id).ValueGeneratedOnAdd();

                    entity.Property(e => e.Name)
                        .IsRequired()
                        .HasMaxLength(20)
                        .IsUnicode(false);
                }
                else
                {
                    entity.HasKey(e => e.Id);
                }
            });
            modelBuilder.Entity<Estados>().ToTable("Estados");
            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
