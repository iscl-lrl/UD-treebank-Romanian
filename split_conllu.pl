use strict;
use warnings;

# Input and output file names
my $input_file = "UD_RoSMSL.conllu";
my $train_file = "UD_RoSMSL-train.conllu";
my $dev_file   = "UD_RoSMSL-dev.conllu";
my $test_file  = "UD_RoSMSL-test.conllu";

# Read the input file
open my $fh, '<', $input_file or die "Could not open file '$input_file' $!";
my @sentences = <$fh>;
close $fh;

# Shuffle the sentences randomly
@sentences = shuffle(\@sentences);

# Calculate the number of sentences for each set
my $total_sentences = scalar @sentences;
my $test_size       = int($total_sentences * 0.125);
my $dev_size        = int($total_sentences * 0.125);
my $train_size      = $total_sentences - $test_size - $dev_size;

# Split the sentences into train, dev, and test sets
my @train_sentences = splice(@sentences, 0, $train_size);
my @dev_sentences   = splice(@sentences, 0, $dev_size);
my @test_sentences  = @sentences;

# Write the sentences to output files
write_to_file($train_file, \@train_sentences);
write_to_file($dev_file, \@dev_sentences);
write_to_file($test_file, \@test_sentences);

# Function to shuffle an array in place
sub shuffle {
    my ($array_ref) = @_;
    for (my $i = @$array_ref - 1; $i > 0; $i--) {
        my $j = int(rand($i + 1));
        @$array_ref[$i, $j] = @$array_ref[$j, $i];
    }
    return @$array_ref;
}

# Function to write sentences to a file
sub write_to_file {
    my ($filename, $sentences_ref) = @_;
    open my $out_fh, '>', $filename or die "Could not open file '$filename' $!";
    print $out_fh @$sentences_ref;
    close $out_fh;
}

print "Splitting complete. Check $train_file, $dev_file, and $test_file.\n";
