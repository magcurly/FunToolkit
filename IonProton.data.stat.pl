#!/usr/bin/perl -w

use strict;
use warnings;

my $path = shift(@ARGV);
my $seqtype= shift(@ARGV);
open OUT,">./stat.xls";
print OUT "\tTotal base\tAssembly Genome Size\tAssembly Coverage\n";
my @prjdir=split /\n/,`ls -d $path/$seqtype*`;
for my $pd(@prjdir){
	#`ls -d $pd/*/`;
	my @dir=split /\n/,`ls -d $pd/*/`;
	for my $d(@dir){
		#print $d;
		next unless -e "$d/00.Raw/240/good.fq.stat";
		my ($tb,$ags,$sample); 
		$sample=(split /\//,$d)[-1]; #get sample name
		open STAT,"$d/00.Raw/240/good.fq.stat";
		<STAT>;
		chomp(my $line=<STAT>); 
		$tb=(split /\s+/,$line)[-1]; #get total base number
		undef $line;
		close STAT;
		open BS,"$d/03.Ass/best.ass";
		chomp(my $bs=<BS>);
		close BS;
		open AST,"$d/03.Ass/ss.txt";
		<AST>;
		while(<AST>){
			chomp;
			if(/^$bs/){
				$ags=(split /\s+/,$_)[2]; #get assembly genome size
				last;
			}
		}
		close AST;
		my $ac=$tb/$ags; #calculate assembly coverage (depth)
		print OUT "$sample\t$tb\t$ags\t$ac\n";
	}
}
close OUT;
print "Done";
	

